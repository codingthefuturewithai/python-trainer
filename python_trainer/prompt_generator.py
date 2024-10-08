from python_trainer.config import UserInfo
from python_trainer.schemas import TrainingPlan

import json

def generate_task_prompt(milestone: dict, user_info: UserInfo, training_plan: TrainingPlan) -> str:
    """
    Generate a prompt for OpenAI GPT to create a practice task based on the milestone,
    user information, and overall training plan.

    Args:
        milestone (dict): The milestone details.
        user_info (UserInfo): The user's information and preferences.
        training_plan (TrainingPlan): The overall training plan.

    Returns:
        str: A formatted prompt for the OpenAI GPT model.
    """
    return f"""
    Create a practice task for the following Python milestone:
    {json.dumps(milestone, indent=2)}

    Consider the following user information:
    {json.dumps(user_info.dict(), indent=2)}

    This milestone is part of the following training plan:
    {json.dumps(training_plan.dict(), indent=2)}

    Please structure your response in the following format:

    1. Concept Explanations:
       - Provide clear and concise explanations of the key concepts related to this milestone.
       - Ensure that all concepts discussed in this section are related to the corresponding practice task and 
         necessary for the learner to understand to accomplish that task.
       - Use examples to illustrate these concepts.
       - Explain how these concepts are used in real-world Python programming.

    2. Practice Task:
       a. A brief introduction to the task
       b. Step-by-step instructions on how to set up the project:
          - Specify if a new project should be created
          - Name the main Python script file
          - List any additional files needed
       c. Detailed requirements for the task
       d. Expected output or behavior
       e. Hints or tips for completing the task
       f. Any additional resources that might be helpful

    Format your response in Markdown, using appropriate headers and formatting for readability.
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

User details:
Experience level: {user_info.programming_experience}
Python knowledge: {user_info.python_experience or 'Not specified'}
Learning goal: {user_info.learning_goal}

REQUIREMENTS:
1. The training plan should focus on practical, hands-on learning with coding exercises and projects.
2. Include theoretical concepts where necessary, but prioritize learning through doing.
3. Each milestone should include both conceptual understanding and practical application.

The plan should include several milestones with milestone names, objectives, and topics to cover. 
Each milestone MUST be tailored to the user's experience level and learning goal.

Provide the response in the following JSON format:

{{
    "background": "A detailed paragraph explaining the rationale behind the training plan based on the user's profile.",
    "milestones": [
        {{
            "name": "Milestone name",
            "objective": "Milestone objective",
            "topics": ["Topic 1", "Topic 2", "Topic 3"],
            "approach": "A detailed description of how this milestone will be tackled, including both conceptual learning and hands-on practice"
        }},
        ...
    ]
}}
"""

    return prompt
