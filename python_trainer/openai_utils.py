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
    try:
        response = openai.chat.completions.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        plan_str = response.choices[0].message.content.strip()
        plan_dict = json.loads(plan_str)
        return TrainingPlan(**plan_dict)
    except json.JSONDecodeError:
        raise ValueError("OpenAI response is not valid JSON")
    except ValueError as e:
        raise ValueError(f"Error parsing OpenAI response: {str(e)}")
    except Exception as e:
        raise Exception(f"Error: Unable to generate training plan. {str(e)}")
