import json
from pathlib import Path

def save_training_plan(training_plan: str, filename: str = "training_plan.json") -> Path:
    """
    Save the training plan to a JSON file.

    Args:
        training_plan (str): The generated training plan.
        filename (str): The name of the file to save the plan to.

    Returns:
        Path: The path where the file was saved.
    """
    save_path = Path.cwd() / filename
    plan_data = {"training_plan": training_plan}
    
    with open(save_path, 'w') as f:
        json.dump(plan_data, f, indent=4)
    
    return save_path
