import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Get the root directory of the project
root_dir = Path(__file__).resolve().parent.parent

# Debug: Print the root directory
print(f"Root directory: {root_dir}")

# Load environment variables from .env file in the root directory
dotenv_path = root_dir / '.env'
print(f"Loading .env from: {dotenv_path}")
load_dotenv(dotenv_path=dotenv_path)

# Debug: Print all environment variables (be careful with this in production!)
print("Environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {'*' * len(value)}")

# Debug: Print the API key (be careful with this in production!)
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key[:5]}...{api_key[-5:] if api_key else 'None'}")

# Set up OpenAI client
client = OpenAI(api_key=api_key)

def get_training_plan(prompt: str) -> str:
    """
    Send a prompt to OpenAI GPT and get a training plan response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The generated training plan from OpenAI GPT.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: Unable to generate training plan. {str(e)}"
