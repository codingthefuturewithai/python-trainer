import os
import json
import openai
from dotenv import load_dotenv
from pathlib import Path
from python_trainer.schemas import TrainingPlan

# Get the root directory of the project
root_dir = Path(__file__).resolve().parent.parent

# Load environment variables from .env file in the root directory
dotenv_path = root_dir / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Set up OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_training_plan(prompt: str) -> TrainingPlan:
    """
    Send a prompt to OpenAI GPT and get a training plan response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        TrainingPlan: The generated training plan from OpenAI GPT, parsed into a TrainingPlan object.
    """
    response = send_openai_request(prompt)
    plan_dict = parse_openai_response(response)
    return TrainingPlan(**plan_dict)

def get_practice_task(prompt: str) -> str:
    """
    Send a prompt to OpenAI GPT and get a practice task response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The generated practice task from OpenAI GPT.
    """
    response = send_openai_request(prompt)
    # Ensure the response is properly formatted as Markdown
    formatted_response = f"# Practice Task\n\n{response.strip()}"
    return formatted_response

def send_openai_request(prompt: str) -> str:
    """
    Send a request to OpenAI GPT and get a response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The response from OpenAI GPT.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Updated to a more recent model
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans and practice tasks."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Error: Unable to generate response from OpenAI. {str(e)}")

def parse_openai_response(response: str) -> dict:
    """
    Parse the OpenAI response into a dictionary.

    Args:
        response (str): The response from OpenAI GPT.

    Returns:
        dict: The parsed response as a dictionary.
    """
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        # If it's not valid JSON, try to extract JSON from the string
        import re
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("Could not extract valid JSON from the response")
