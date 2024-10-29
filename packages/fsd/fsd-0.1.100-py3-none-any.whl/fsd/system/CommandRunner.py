import subprocess
import os
import sys
import requests
import psutil
import threading
import json
from log.logger_config import get_logger
from .FileContentManager import FileContentManager
from .OSEnvironmentDetector import OSEnvironmentDetector
from .ConfigAgent import ConfigAgent
from .TaskErrorPlanner import TaskErrorPlanner
import time
import signal
from typing import Tuple, List
from pathlib import Path
import os
import platform
logger = get_logger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.utils import parse_payload

class CommandRunner:
    def __init__(self, repo):
        """
        Initializes the CommandRunner.
        """
        self.repo = repo
        self.config = ConfigAgent(repo)
        self.errorPlanner = TaskErrorPlanner(repo)
        self.config_manager = FileContentManager()  # Initialize CodeManager in the constructor
        self.detector = OSEnvironmentDetector()
        self.directory_path = repo.get_repo_path()
        self.max_retry_attempts = 3  # Set a maximum number of retry attempts

    async def get_config_requests(self, instructions, file_name):
        """Generate coding requests based on instructions and context."""

        main_path = file_name
        logger.debug(f" #### The `ConfigAgent` is initiating the processing of file: {file_name} in {main_path}")
        logger.info(f" #### The `ConfigAgent` has been assigned the following task: {instructions}")
        result = await self.config.get_config_requests(instructions, main_path)
        if main_path:
            await self.config_manager.handle_coding_agent_response(main_path, result)
            logger.info(f" #### The `Config Agent` has successfully completed its work on {file_name}")
        else:
            logger.debug(f" #### The `ConfigAgent` encountered an issue: Unable to locate the file: {file_name}")

    async def get_error_planner_requests(self, error, config_context, os_architecture, compile_files, original_prompt_language):
        """Generate coding requests based on instructions and context."""
        result = await self.errorPlanner.get_task_plans(error, config_context, os_architecture, compile_files, original_prompt_language)
        return result

    def run_command(self, command: str, method: str = 'bash', inactivity_timeout: int = 5, use_timeout: bool = True) -> Tuple[int, List[str]]:
        """
        Runs a given command using the specified method.
        Shows real-time output during execution within a Bash markdown block.
        Returns a tuple of (return_code, all_output).
        Implements an optional inactivity timeout to determine command completion.
        
        Parameters:
        - command (str): The shell command to execute.
        - method (str): The shell method to use (default is 'bash').
        - inactivity_timeout (int): Seconds to wait for new output before considering done.
        - use_timeout (bool): Whether to enforce the inactivity timeout.
        """
        markdown_block_open = False  # Flag to track if markdown block is open
        process = None  # Initialize process variable

        try:
            # Use bash for all commands
            shell = True
            executable = '/bin/bash'

            # Check if the command is a 'cd' command
            if command.startswith('cd '):
                # Change the working directory
                new_dir = command[3:].strip()
                os.chdir(new_dir)
                logger.info(
                    f"#### Directory Change\n"
                    f"```bash\nChanged directory to: {new_dir}\n```\n"
                    f"----------------------------------------"
                )
                return 0, [f"Changed directory to: {new_dir}"]

            # Log the current working directory and the command to be executed
            current_path = os.getcwd()
            logger.info(
                f"#### Executing Command\n"
                f"```bash\n{command}\n```\n"
                f"**In Directory:** `{current_path}`\n"
                f"#### Command Output\n```bash"
            )
            markdown_block_open = True  # Code block is now open

            # Start the process in a new session to create a new process group
            process = subprocess.Popen(
                command,
                shell=shell,
                executable=executable,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=current_path,  # Explicitly set the working directory
                start_new_session=True  # Start the process in a new session
            )

            # Use psutil to handle process and its children
            parent = psutil.Process(process.pid)

            # Initialize output list
            output = []

            # Variable to track the last time output was received
            last_output_time = time.time()

            # Lock for thread-safe updates to last_output_time
            lock = threading.Lock()

            # Function to read output
            def read_output(stream, output_list):
                nonlocal markdown_block_open, last_output_time
                for line in iter(stream.readline, ''):
                    line = line.rstrip()
                    output_list.append(line)
                    logger.info(line)
                    with lock:
                        last_output_time = time.time()
                stream.close()

            # Start threads to read stdout and stderr
            stdout_thread = threading.Thread(target=read_output, args=(process.stdout, output))
            stderr_thread = threading.Thread(target=read_output, args=(process.stderr, output))
            stdout_thread.start()
            stderr_thread.start()

            # Monitoring loop
            while True:
                if process.poll() is not None:
                    # Process has finished
                    break
                if use_timeout:
                    with lock:
                        time_since_last_output = time.time() - last_output_time
                    if time_since_last_output > inactivity_timeout:
                        # No output received within the inactivity timeout
                        logger.info(f"No output received for {inactivity_timeout} seconds. Assuming command completion.")
                        break
                time.sleep(0.1)  # Prevent busy waiting

            # If the process is still running, attempt to terminate it gracefully
            if process.poll() is None:
                try:
                    logger.info(f"Attempting to terminate the subprocess after inactivity timeout of {inactivity_timeout} seconds.")
                    # Terminate the subprocess
                    process.terminate()

                    try:
                        process.wait(timeout=5)
                        logger.info("Subprocess terminated gracefully.")
                    except subprocess.TimeoutExpired:
                        logger.info("Subprocess did not terminate in time; killing it.")
                        process.kill()

                except Exception as e:
                    logger.error(f"Error terminating the subprocess: {e}")

            # Wait for threads to finish reading
            stdout_thread.join()
            stderr_thread.join()

            # Close the markdown code block if it's open
            if markdown_block_open:
                logger.info("```")  # Close the markdown block
                markdown_block_open = False

            return_code = process.returncode
            logger.info(
                f"#### Command Finished with Return Code: `{return_code}`\n"
                f"----------------------------------------"
            )
            logger.info("The `CommandRunner` has completed the current step and is proceeding to the next one.")
            return return_code, output

        except Exception as e:
            logger.error(f"An error occurred while running the command: {e}")
            # Ensure that the subprocess is terminated in case of an exception
            if process and process.poll() is None:
                try:
                    logger.info("Attempting to terminate the subprocess due to an exception.")
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        logger.info("Subprocess did not terminate in time; killing it.")
                        process.kill()
                except Exception as terminate_error:
                    logger.error(f"Failed to terminate subprocess after exception: {terminate_error}")
            return -1, [f"An error occurred: {e}"]

    def update_file(self, file_name, content):
        """
        Updates the content of a file.
        """
        try:
            with open(file_name, 'a') as file:
                file.write(content + '\n')
            logger.info(f" #### The `CommandRunner` has successfully updated the file: {file_name}")
            return f"Successfully updated {file_name}"
        except Exception as e:
            logger.error(f" #### The `CommandRunner` encountered an error while attempting to update {file_name}: {str(e)}")
            return f"Failed to update {file_name}: {str(e)}"
        
    def open_terminal(self, bash_command):
        """
        Opens a terminal window, navigates to the project path, and runs the specified bash command.

        Parameters:
            bash_command (str): The bash command to execute in the terminal.
        """
        # Retrieve the project path
        project_path = self.repo.get_repo_path()
        logger.info(f"#### Project Path: `{project_path}`")
        logger.info(f" #### Bash Command: `{bash_command}`")

        # Ensure the project path exists
        if not Path(project_path).exists():
            logger.error(f"The project path does not exist: {project_path}")
            raise FileNotFoundError(f"The project path does not exist: {project_path}")

        # Detect the operating system
        current_os = platform.system()
        logger.info(f"Operating System Detected: {current_os}")

        try:
            if current_os == 'Windows':
                self._open_terminal_windows(project_path, bash_command)
            elif current_os == 'Darwin':
                self._open_terminal_mac(project_path, bash_command)
            else:
                logger.error(f"Unsupported Operating System: {current_os}")
                raise NotImplementedError(f"OS '{current_os}' is not supported.")
        except Exception as e:
            logger.exception(f"Failed to open terminal: {e}")
            raise

    def _open_terminal_windows(self, project_path, bash_command):
        """
        Opens Command Prompt on Windows, navigates to the project path, and runs the bash command.

        Parameters:
            project_path (str): The path to navigate to.
            bash_command (str): The command to execute.
        """
        # Construct the command to open cmd.exe, change directory, and execute the bash command
        # The /k flag keeps the window open after the command executes
        cmd = f'start cmd.exe /k "cd /d "{project_path}" && {bash_command}"'
        logger.debug(f"Windows CMD Command: {cmd}")

        # Execute the command
        subprocess.Popen(cmd, shell=True)
        logger.info("#### `Command Prompt` opened successfully.")

    def _open_terminal_mac(self, project_path, bash_command):
        """
        Opens Terminal.app on macOS, navigates to the project path, and runs the bash command.

        Parameters:
            project_path (str): The path to navigate to.
            bash_command (str): The command to execute.
        """
        # AppleScript to open a new Terminal window, navigate to the directory, and run the command
        apple_script = f'''
        tell application "Terminal"
            activate
            do script "cd \\"{project_path}\\"; {bash_command}"
        end tell
        '''
        logger.debug(f"AppleScript: {apple_script}")

        # Execute the AppleScript
        subprocess.Popen(['osascript', '-e', apple_script])
        logger.info("#### `Terminal.app` opened successfully.")

    async def execute_steps(self, steps_json, compile_files, original_prompt_language):
        """
        Executes a series of steps provided in JSON format.
        Asks for user permission before executing each step.
        Waits for each command to complete before moving to the next step.
        """
        steps = steps_json['steps']

        for step in steps:
            is_localhost_command = step.get('is_localhost_command', "0")
            if step['method'] == 'bash':
                logger.info(f"#### `Command Runner`: {step['prompt']}")
                logger.info(f"```bash\n{step['command']}\n```")
            elif step['method'] == 'update':
                logger.info(f"#### `Command Runner`:")
                logger.info(f"```yaml\n{step['prompt']}\n```")

            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
            user_permission = input()

            user_prompt, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_permission)
            user_prompt = user_prompt.lower()

            if user_prompt == 'exit':
                logger.info(" #### The user has chosen to exit. The `CommandRunner` is halting execution.")
                return "Execution stopped by user"
            elif user_prompt == 's':
                logger.info(" #### The user has chosen to skip this step.")
                continue

            logger.info(f" #### The `CommandRunner` is now executing the following step: {step['prompt']}")

            retry_count = 0
            while retry_count < self.max_retry_attempts:
                if step['method'] == 'bash':
                    # Run the command and get the return code and output
                    return_code, command_output = self.run_command(step['command'])

                    # Check for errors based on the return code
                    if return_code != 0 and return_code != None:
                        error_message = ','.join(command_output)
                        logger.error(f" #### The `CommandRunner` reports: Command execution failed with return code {return_code}: {error_message}")
                        
                        # Check if the error suggests an alternative command
                        if "Did you mean" in error_message:
                            suggested_command = error_message.split("Did you mean")[1].strip().strip('"?')
                            logger.info(f" #### `SystemSuggestionHandler` has found an alternative command: {suggested_command}")
                            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                            user_choice = input()

                            user_select, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_choice)
                            user_select = user_select.lower()
                            
                            if user_select == 'a':
                                logger.info(f" #### `UserInteractionHandler`: Executing suggested command: {suggested_command}")
                                return_code, command_output = self.run_command(suggested_command)
                                if return_code == 0 or return_code == None:
                                    if is_localhost_command == "1" or is_localhost_command == 1:
                                        logger.info(
                                            f"#### `Command agent` believes this is localhost `{suggested_command}`. "
                                            "It has run successfully, so there is potentially no error. "
                                            "However, I have already shut it down. We can open it separately in your terminal."
                                        )
                                        logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                                        user_run = input()

                                        user_select_run, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_run)
                                        user_select_run = user_select_run.lower()
                                        if user_select_run == 'a':
                                            self.open_terminal(suggested_command)
                                        break
                                    else:
                                        break  # Command executed successfully
                                else:
                                    # Update error_message with new command output
                                    error_message = ','.join(command_output)
                                    logger.error(
                                        f"#### `CommandExecutor`: Suggested command also failed with return code {return_code}: {error_message}")
                            elif user_select == 'exit':
                                logger.info(" #### `UserInteractionHandler`: User has chosen to exit. Stopping execution.")
                                return "Execution stopped by user"
                            else:
                                logger.info(" #### `UserInteractionHandler`: User chose not to run the suggested command.")
                        
                        # Proceed to handle the error
                        fixing_steps = await self.get_error_planner_requests(error_message, step['prompt'], self.detector, compile_files, original_prompt_language)
                        fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, original_prompt_language)
                        if fixing_result == "Execution stopped by user":
                            logger.info(" #### The user has chosen to exit during the fixing steps. The `CommandRunner` is skipping the current step.")
                            break
                        retry_count += 1
                    else:
                        if is_localhost_command == "1" or is_localhost_command == 1:
                            logger.info(
                                f"#### `Command agent` believes this is localhost `{step['command']}`. "
                                "It has run successfully, so there is potentially no error. "
                                "However, I have already shut it down. We can open it separately in your terminal."
                            )
                            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                            user_run = input()

                            user_select_run, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_run)
                            user_select_run = user_select_run.lower()
                            if user_select_run == 'a':
                                self.open_terminal(step['command'])
                            break
                        else:
                           break
                elif step['method'] == 'update':
                    file_name = step.get('file_name', '')
                    if file_name != 'N/A':
                        await self.get_config_requests(step['prompt'], file_name)
                        logger.info(f" #### The `CommandRunner` has successfully updated the file: {file_name}")
                    else:
                        logger.debug("\n #### The `CommandRunner` reports: Update method specified but no file name provided.")
                    break
                else:
                    logger.error(f" #### The `CommandRunner` encountered an unknown method: {step['method']}")
                    break

            if retry_count == self.max_retry_attempts:
                logger.error(f" #### The `CommandRunner` reports: Step failed after {self.max_retry_attempts} attempts: {step['prompt']}")
                error_message = f"Step failed after {self.max_retry_attempts} attempts: {step['prompt']}"
                fixing_steps = await self.get_error_planner_requests(error_message, step['prompt'], self.detector, compile_files, original_prompt_language)
                fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files)
                if fixing_result == "Execution stopped by user":
                    logger.info(" #### The user has chosen to exit during the fixing steps. The `CommandRunner` is skipping the current step.")
                    continue
                return f"Step failed after {self.max_retry_attempts} attempts: {step['prompt']}"

            logger.info(" #### The `CommandRunner` has completed the current step and is proceeding to the next one.")

        logger.info(" #### The `CommandRunner` has successfully completed all steps")
        return "All steps completed successfully"

    async def execute_fixing_steps(self, steps_json, compile_files, original_prompt_language):
        """
        Executes a series of steps provided in JSON format to fix dependency issues.
        Asks for user permission before executing each step.
        Waits for each command to complete before moving to the next step.
        """
        steps = steps_json['steps']

        for step in steps:

            if step['method'] == 'bash':
                logger.info(f" #### `Command Runner`: {step['error_resolution']}")
                logger.info(f"```bash\n{step['command']}\n```")
            elif step['method'] == 'update':
                logger.info(f" #### `Command Runner`:")
                logger.info(f"```yaml\n{step['error_resolution']}\n```")
           
            logger.info("")
            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
            user_permission = input()

            user_prompt, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_permission)
            user_prompt = user_prompt.lower()

            if user_prompt == 'exit':
                logger.info(" #### The user has chosen to exit. The `CommandRunner` is halting execution.")
                return "Execution stopped by user"
            elif user_prompt == 's':
                logger.info(" #### The user has chosen to skip this step.")
                continue

            logger.info(f" #### The `CommandRunner` is now executing the following fixing step: {step['error_resolution']}")

            retry_count = 0
            while retry_count < self.max_retry_attempts:
                if step['method'] == 'bash':
                    # Run the command and get the return code and output
                    return_code, command_output = self.run_command(step['command'])
                    
                    # Check for errors based on the return code
                    if return_code != 0:
                        error_message = ','.join(command_output)
                        logger.error(f" #### The `CommandRunner` reports: Command execution failed with return code {return_code}: {error_message}")

                        # Check if the error suggests an alternative command
                        if "Did you mean" in error_message:
                            suggested_command = error_message.split("Did you mean")[1].strip().strip('"?')
                            logger.info(f" #### `SystemSuggestionHandler` has found an alternative command: {suggested_command}")
                            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                            user_choice = input()

                            user_select, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_choice)
                            user_select = user_select.lower()
                            
                            if user_select == 'a':
                                logger.info(f" #### `UserInteractionHandler`: Executing suggested command: {suggested_command}")
                                return_code, command_output = self.run_command(suggested_command)
                                if return_code == 0:
                                    break  # Command executed successfully
                                else:
                                    # Update error_message with new command output
                                    error_message = ','.join(command_output)
                                    logger.error(
                                        f"\n #### `CommandExecutor`: Suggested command also failed with return code {return_code}: {error_message}")
                            elif user_select == 'exit':
                                logger.info(" #### `UserInteractionHandler`: User has chosen to exit. Stopping execution.")
                                return "Execution stopped by user"
                            else:
                                logger.info(" #### `UserInteractionHandler`: User chose not to run the suggested command.")
                        
                        # Proceed to handle the error
                        fixing_steps = await self.get_error_planner_requests(error_message, step['error_resolution'], self.detector, compile_files, original_prompt_language)
                        fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, original_prompt_language)
                        if fixing_result == "Execution stopped by user":
                            return "Execution stopped by user"
                        retry_count += 1
                    else:
                        break  # Command executed successfully without errors
                elif step['method'] == 'update':
                    file_name = step.get('file_name', '')
                    if file_name != 'N/A':
                        await self.get_config_requests(step['error_resolution'], file_name)
                        logger.info(f" #### The `CommandRunner` has successfully updated the file: {file_name}")
                    else:
                        logger.debug("\n #### The `CommandRunner` reports: Update method specified but no file name provided.")
                    break
                else:
                    logger.error(f" #### The `CommandRunner` encountered an unknown method: {step['method']}")
                    break

            if retry_count == self.max_retry_attempts:
                logger.error(f" #### The `CommandRunner` reports: Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}")
                error_message = f"Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}"
                fixing_steps = await self.get_error_planner_requests(error_message, step['error_resolution'], self.detector, compile_files, original_prompt_language)
                fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, original_prompt_language)
                if fixing_result == "Execution stopped by user":
                    return "Execution stopped by user"
                return f"Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}"

            logger.info(" #### The `CommandRunner` has completed the current fixing step and is proceeding to the next one.")

        logger.info(" #### The `CommandRunner` has successfully completed all fixing steps")
        return "All fixing steps completed successfully"