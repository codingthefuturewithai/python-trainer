from python_trainer.config import UserInfo

import json

def generate_task_prompt(milestone: dict) -> str:
    """
    Generate a prompt for OpenAI GPT to create a practice task based on the milestone.

    Args:
        milestone (dict): The milestone details.

    Returns:
        str: A formatted prompt for the OpenAI GPT model.
    """
    return f"""
    Create a practice task for the following Python milestone:
    {json.dumps(milestone, indent=2)}

    Please include the following in your response:
    1. A brief introduction to the task
    2. Step-by-step instructions on how to set up the project:
       - Specify if a new project should be created
       - Name the main Python script file
       - List any additional files needed
    3. Detailed requirements for the task
    4. Expected output or behavior
    5. Hints or tips for completing the task
    6. Any additional resources that might be helpful

    Format your response in Markdown.
    """

def generate_prompt(user_info: UserInfo) -> str:
    """
    Generate a prompt for OpenAI GPT based on user information.
    
    Args:
        user_info (UserInfo): User information collected from CLI.
    
    Returns:
        str: A formatted prompt for the OpenAI GPT model.
    """
    prompt = f"""Create a Python training plan for a user with the following profile:
Experience level: {user_info.programming_experience}
Python knowledge: {user_info.python_experience or 'Not specified'}
Learning goal: {user_info.learning_goal}
Preferred learning style: {user_info.learning_style}

The plan should include several milestones with milestone names, objectives, and topics to cover. 
Each milestone should be tailored to the user's experience level and learning style.
Provide the response in the following JSON format:

{{
    "background": "A brief paragraph explaining the rationale behind the training plan based on the user's profile",
    "milestones": [
        {{
            "name": "Milestone name",
            "objective": "Milestone objective",
            "topics": ["Topic 1", "Topic 2", "Topic 3"]
        }},
        ...
    ]
}}
"""

    return prompt
