import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: Unable to generate training plan. {str(e)}"
