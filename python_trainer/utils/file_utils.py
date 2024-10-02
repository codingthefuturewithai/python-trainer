from pathlib import Path

def save_training_plan(training_plan: str, filename: str = "training_plan.md") -> Path:
    """
    Save the training plan to a Markdown file.

    Args:
        training_plan (str): The generated training plan.
        filename (str): The name of the file to save the plan to.

    Returns:
        Path: The path where the file was saved.
    """
    save_path = Path.cwd() / filename
    
    with open(save_path, 'w') as f:
        f.write("# Python Training Plan\n\n")
        f.write(training_plan)
    
    return save_path
