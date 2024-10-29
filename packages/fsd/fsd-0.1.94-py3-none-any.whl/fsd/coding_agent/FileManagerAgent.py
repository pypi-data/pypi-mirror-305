import os
import aiohttp
import asyncio
import json
import sys
from json_repair import repair_json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

from fsd.util.utils import read_file_content
from fsd.util.utils import process_image_files
from fsd.PromptImageUrlAgent.PromptImageUrlAgent import PromptImageUrlAgent
class FileManagerAgent:
    def __init__(self, repo):
        """
        Initialize the FileManagerAgent with directory path, API key, endpoint, deployment ID, and max tokens for API requests.

        Args:
            directory_path (str): Path to the directory containing .txt files.
            api_key (str): API key for Azure OpenAI API.
            endpoint (str): Endpoint URL for Azure OpenAI.
            deployment_id (str): Deployment ID for the model.
            max_tokens (int): Maximum tokens for the Azure OpenAI API response.
        """
        self.repo = repo
        self.max_tokens = 4096
        self.imageAgent = PromptImageUrlAgent(repo)
        self.ai = AIGateway()

    async def get_file_planning(self, idea):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            idea (str): The general plan idea.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the plan or an error reason.
        """
            # Start of Selection
        prompt = (
                "From the provided development plan, build a JSON to add new files to be created and list Existing_files and Context_files as specified in the instruction. Provide only a JSON response without any additional text or Markdown formatting. "
                "Adding_new_files must include only new files explicitly mentioned in the instruction that need to be created, including all .md files if specified. IMPORTANT: Never skip .md or documentation files like README.md etc. Strictly exclude ALL dependency configuration files (such as requirements.txt, package.json, Podfile, yarn.lock, Gemfile, etc.) from Adding_new_files. These will be handled separately later. For image files, only include .svg files if mentioned. Ignore all png, jpg, jpeg image file types for adding new files. "
                "Moving_files must include existing files that are explicitly mentioned in the instruction to be moved from a specific location A to a specific location B within the project. Do not include any files in Moving_files unless the instruction clearly states to move an existing file from one location to another."
                "Existing_files must include only the full paths for file names explicitly mentioned in the instruction that will be updated or modified. "
                "Context_files must include only the full path context file names explicitly mentioned in the instruction that provide context but won't be modified. Existing_files and Context_files must not overlap. Exclude all dependency files, configuration files, and non-code files such as .gitignore, package.json, Podfile, etc. Focus on including only relevant code files. "
                "If no file needs to be created or no file needs to be moved, follow this JSON format:\n"
                "{\n"
                "    \"Is_creating\": false,\n"
                "    \"Existing_files\": [\"/full/path/to/file1.extension\", \"/full/path/to/file2.extension\"],\n"
                "    \"Context_files\": [\"/full/path/to/file3.extension\", \"/full/path/to/file4.extension\"],\n"
                "    \"Adding_new_files\": []\n"
                "    \"Moving_files\": []\n"
                "}\n\n"
                "If there are files that will need to be created, follow this JSON format:\n"
                "Pipeline should follow this rule, choose either 1 or 2 that most fits:\n"
                "1. If this is an Xcode project.\n"
                "2. If this is not an Xcode project.\n"
                "{\n"
                "    \"commits\": "",\n"
                "    \"Is_creating\": true,\n"
                "    \"Existing_files\": [\"/full/path/to/file1.extension\", \"/full/path/to/file2.extension\"],\n"
                "    \"Context_files\": [\"/full/path/to/file3.extension\", \"/full/path/to/file4.extension\"],\n"
                "    \"Adding_new_files\": [\n"
                "        {\n"
                "            \"Pipeline\": \"1 or 2\",\n"
                "            \"Function_to_call\": \"create_and_add_file_to_xcodeproj\",\n"
                "            \"Parameters\": {\n"
                "                \"full_path\": \"/exact/path/from/development/plan/including/project/folder/example.extension\"\n"
                "            }\n"
                "        }\n"
                "    ],\n"
                "    \"Moving_files\": [\n"
                "        {\n"
                "            \"Function_to_call\": \"move_file_within_xcodeproj\",\n"
                "            \"Pipeline\": \"1 or 2\",\n"
                "            \"Parameters\": {\n"
                "                \"old_full_path\": \"/full/path/to/old/location/example.extension\",\n"
                "                \"new_full_path\": \"/full/path/to/new/location/example.extension\"\n"
                "            }\n"
                "        }\n"
                "    ]\n"
                "}\n\n"
                "Existing_files, Context_files, and Adding_new_files must include only files explicitly mentioned in the instruction.\n"
                "full_path must be the exact path as specified in the development plan, without any modifications. Do not ignore or omit the project folder name (such as projectA, projectB) as it is crucial for the correct path.\n"
                f"The project root path is \"{self.repo.get_repo_path()}\"\n"
                "DO NOT CREATE ANY NEW jpg, jpeg, PNG, JPG, JPEG, .ico, OR ANY VIDEO FILE TYPES."
                "FOR ALL TYPES OF ASSETS, ONLY CREATE AND GENERATE NEW SVG IMAGES."
                "CRITICAL: Do NOT include any dependency configuration files in Adding_new_files under any circumstances. These will be handled in a separate process.\n"
                "IMPORTANT: Strictly adhere to the development plan. For Adding_new_files, never create new paths or folders not explicitly mentioned in the plan. Do not invent or hallucinate any file paths or names. Only include files and paths that are exactly as specified in the development plan, including the project folder name."
                "Return only valid JSON without Markdown symbols or invalid escapes.\n"
                "Generate a commit message for the adding/moving files if need. The commit message must use the imperative tense and be structured as follows: <type>: <description>. Use these for <type>: bugfix, feature, optimize, update, config, document, format, restructure, enhance, verify. The commit message should be a single line.\n"
                "CRITICAL: Do NOT create any new folders standalone. Only create eligible files."
            )

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": f"This is the development plan:\n{idea}\nThis is the current project structure:\n{self.repo.print_tree()}\n"
            }
        ]

        try:
            logger.debug("\n #### The `FileManagerAgent` is initiating a request to the AI for file planning")
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            logger.debug("\n #### The `FileManagerAgent` has successfully received a response from the AI")
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            logger.debug("\n #### The `FileManagerAgent` encountered a JSON decode error and is attempting to repair it")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.debug(f" #### The `FileManagerAgent` encountered an unexpected error: `{e}`")
            return {
                "reason": str(e)
            }


    async def get_adding_file_planning(self, idea, tree, file_attachments):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the plan or an error reason.
        """
        prompt = (
            "Create JSON for new files from development plan. JSON only, no extra text or Markdown. "
            "Include all new files in Adding_new_files. "
            "Pipeline: 1 for Xcode, 2 for non-Xcode. "
            "Use this format:\n"
            "{\n"
            "    \"Is_creating\": true,\n"
            "    \"commits\": "",\n"
            "    \"Adding_new_files\": [\n"
            "        {\n"
            "            \"Title\": \"Creating a new file\",\n"
            "            \"Function_to_call\": \"create_and_add_file_to_xcodeproj\",\n"
            "            \"Pipeline\": \"1 or 2\",\n"
            "            \"Parameters\": {\n"
            "                \"full_path\": \"" + self.repo.get_repo_path() + "full_relative_path/example.extension\"\n"
            "            }\n"
            "        }\n"
            "    ]\n"
            "}\n"
            "For folders only, use full path ending with '/'. "
            f"project_root_path must be \"{self.repo.get_repo_path()}\". "
            "Generate a commit message for the adding files if need. The commit message must use the imperative tense and be structured as follows: <type>: <description>. Use these for <type>: bugfix, feature, optimize, update, config, document, format, restructure, enhance, verify. The commit message should be a single line.\n"
            "Ensure all paths are correct and complete. Use only valid JSON without Markdown or escapes."
        )

        all_attachment_file_contents = ""

        # Process image files
        image_files = process_image_files(file_attachments)
        
        # Remove image files from file_attachments
        file_attachments = [f for f in file_attachments if not f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png'))]

        if file_attachments:
            for file_path in file_attachments:
                file_content = read_file_content(file_path)
                if file_content:
                    all_attachment_file_contents += f"\n\nFile: {os.path.relpath(file_path)}:\n{file_content}"

        if all_attachment_file_contents:
            prompt += f"User has attached these files, use them appropriately: {all_attachment_file_contents}"

        image_result = await self.imageAgent.process_image_links(idea)
        assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []

        user_content = [{"type": "text", "text": prompt}]

        # Add image files to the user content
        for base64_image in image_files:
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"{base64_image}"
                }
            })

        if assets_link:
            for image_url in assets_link:
                user_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                })

        messages = [
            {
                "role": "system",
                "content": user_content
            },
            {
                "role": "user",
                "content": f"This is the development plan:\n{idea}\nThis is the current project structure:\n{tree}\n"
            }
        ]

        try:
            logger.debug("\n #### The `FileManagerAgent` is commencing the process of adding file planning")
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            logger.debug("\n #### The `FileManagerAgent` has successfully completed the adding file planning process")
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            logger.debug("\n #### The `FileManagerAgent` encountered a JSON decode error and is attempting to repair it")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.debug(f" #### The `FileManagerAgent` encountered an unexpected error during adding file planning: `{e}`")
            return {
                "reason": str(e)
            }


    async def get_moving_file_planning(self, idea, tree, file_attachments):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the plan or an error reason.
        """
        prompt = (
            "Generate JSON for moving files based on the development plan. Include all files to be moved. "
            "Pipeline: 1 for Xcode project, 2 for non-Xcode. "
            "Use this format for files to move:\n"
            "{\n"
            "    \"Is_moving\": true,\n"
            "    \"commits\": "",\n"
            "    \"Moving_files\": [\n"
            "        {\n"
            "            \"Title\": \"Moving a file\",\n"
            "            \"Function_to_call\": \"move_file_within_xcodeproj\",\n"
            "            \"Pipeline\": \"1 or 2\",\n"
            "            \"Parameters\": {\n"
            "                \"old_full_path\": \"/full/path/to/old/location/example.extension\",\n"
            "                \"new_full_path\": \"/full/path/to/new/location/example.extension\"\n"
            "            }\n"
            "        }\n"
            "    ]\n"
            "}\n"
            "For folders, include the full path to the folder. "
            f"All paths must start with \"{self.repo.get_repo_path()}\". "
            "Generate a commit message for the moving files if need. The commit message must use the imperative tense and be structured as follows: <type>: <description>. Use these for <type>: bugfix, feature, optimize, update, config, document, format, restructure, enhance, verify. The commit message should be a single line.\n"
            "Ensure all paths are correct and complete. Use only valid JSON without Markdown or escapes."
        )

        all_attachment_file_contents = ""

        # Process image files
        image_files = process_image_files(file_attachments)
        
        # Remove image files from file_attachments
        file_attachments = [f for f in file_attachments if not f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png'))]

        if file_attachments:
            for file_path in file_attachments:
                file_content = read_file_content(file_path)
                if file_content:
                    all_attachment_file_contents += f"\n\nFile: {os.path.relpath(file_path)}:\n{file_content}"

        if all_attachment_file_contents:
            prompt += f"User has attached these files, use them appropriately: {all_attachment_file_contents}"
        

        image_result = await self.imageAgent.process_image_links(idea)
        assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []

        user_content = [{"type": "text", "text": prompt}]

        # Add image files to the user content
        for base64_image in image_files:
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"{base64_image}"
                }
            })

        if assets_link:
            for image_url in assets_link:
                user_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                })

        messages = [
            {
                "role": "system",
                "content": user_content
            },
            {
                "role": "user",
                "content": f"This is the development plan:\n{idea}\nThis is the current project structure:\n{tree}\n"
            }
        ]

        try:
            logger.debug("\n #### The `FileManagerAgent` is initiating the process of moving file planning")
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            logger.debug("\n #### The `FileManagerAgent` has successfully completed the moving file planning process")
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            logger.debug("\n #### The `FileManagerAgent` encountered a JSON decode error and is attempting to repair it")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.debug(f" #### The `FileManagerAgent` encountered an unexpected error during moving file planning: `{e}`")
            return {
                "reason": str(e)
            }

    async def get_moving_file_plannings(self, idea, tree, file_attachments):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (list): List of file paths representing the project structure.

        Returns:
            dict: JSON response with the plan.
        """
        logger.debug("\n #### The `FileManagerAgent` is beginning the process of retrieving moving file plannings")
        all_file_contents = self.repo.print_tree()

        plan = await self.get_moving_file_planning(idea, all_file_contents, file_attachments)
        logger.debug("\n #### The `FileManagerAgent` has successfully retrieved the moving file plannings")
        return plan

    async def get_adding_file_plannings(self, idea, tree, file_attachments):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (list): List of file paths representing the project structure.

        Returns:
            dict: JSON response with the plan.
        """
        logger.debug("\n #### The `FileManagerAgent` is commencing the process of retrieving adding file plannings")
        all_file_contents = self.repo.print_tree()

        plan = await self.get_adding_file_planning(idea, all_file_contents, file_attachments)
        logger.debug("\n #### The `FileManagerAgent` has successfully retrieved the adding file plannings")
        return plan

    async def get_file_plannings(self, idea):
        """
        Request file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (list): List of file paths representing the project structure.

        Returns:
            dict: JSON response with the plan.
        """
        logger.debug("\n #### The `FileManagerAgent` is initiating the process of retrieving file plannings")
        plan = await self.get_file_planning(idea)
        logger.debug("\n #### The `FileManagerAgent` has successfully retrieved the file plannings")
        return plan