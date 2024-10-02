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
            model="gpt-4-0613",  # Updated to a more recent model
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans in JSON format."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
        )
        plan_str = response.choices[0].message.content.strip()
        
        # Try to extract JSON from the response if it's not pure JSON
        try:
            plan_dict = json.loads(plan_str)
        except json.JSONDecodeError:
            # If it's not valid JSON, try to extract JSON from the string
            import re
            json_match = re.search(r'\{.*\}', plan_str, re.DOTALL)
            if json_match:
                plan_dict = json.loads(json_match.group())
            else:
                raise ValueError("Could not extract valid JSON from the response")
        
        return TrainingPlan(**plan_dict)
    except json.JSONDecodeError as e:
        raise ValueError(f"OpenAI response is not valid JSON: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Error parsing OpenAI response: {str(e)}")
    except Exception as e:
        raise Exception(f"Error: Unable to generate training plan. {str(e)}")
