import os
import openai
from dotenv import load_dotenv
from pathlib import Path

# Get the root directory of the project
root_dir = Path(__file__).resolve().parent.parent

# Load environment variables from .env file in the root directory
dotenv_path = root_dir / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Set up OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_training_plan(prompt: str) -> str:
    """
    Send a prompt to OpenAI GPT and get a training plan response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The generated training plan from OpenAI GPT.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                    {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans."},
                    {"role": "user", "content": prompt}
                ],
            # max_tokens=1000,
            # n=1,
            temperature=0.1,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: Unable to generate training plan. {str(e)}"
