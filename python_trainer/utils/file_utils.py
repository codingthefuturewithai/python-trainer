from pathlib import Path

def save_training_plan(training_plan: str, filename: str) -> Path:
    """
    Save the training plan to a Markdown file.

    Args:
        training_plan (str): The formatted training plan as a string.
        filename (str): The name of the file to save the plan to.

    Returns:
        Path: The path where the file was saved.
    """
    save_path = Path.cwd() / filename
    
    with open(save_path, 'w') as f:
        f.write(training_plan)
    
    return save_path
