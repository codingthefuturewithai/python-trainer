from pathlib import Path

def create_output_directory() -> Path:
    """
    Create a dedicated directory for organizing saved files.

    Returns:
        Path: The path to the created directory.
    """
    output_dir = Path("python_trainer_output")
    output_dir.mkdir(exist_ok=True)
    return output_dir.resolve()

def save_training_plan(training_plan: str, filename: str) -> Path:
    """
    Save the training plan to a Markdown file in the dedicated output directory.

    Args:
        training_plan (str): The formatted training plan as a string.
        filename (str): The name of the file to save the plan to.

    Returns:
        Path: The path where the file was saved.
    """
    output_dir = create_output_directory()
    save_path = output_dir / filename
    
    with open(save_path, 'w') as f:
        f.write(training_plan)
    
    return save_path
