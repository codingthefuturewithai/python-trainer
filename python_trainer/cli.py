import click
from python_trainer.config import UserInfo

def prompt_with_choices(text, choices):
    choice_text = '\n'.join(f'{i+1}) {choice}' for i, choice in enumerate(choices))
    while True:
        click.echo(f"{text}\n{choice_text}")
        choice = click.prompt("Enter the number of your choice", type=int)
        if 1 <= choice <= len(choices):
            return choices[choice - 1]
        click.echo(f"Invalid choice. Please enter a number between 1 and {len(choices)}.")

def prompt_yes_no(question: str) -> bool:
    """Prompt the user for a yes/no response."""
    return click.confirm(question, default=True)

def gather_user_info() -> UserInfo:
    """Gather user information through CLI prompts."""
    programming_experience = prompt_with_choices(
        "What is your programming experience?",
        ["No programming experience", "Experienced programmer new to Python"]
    )
    
    python_experience = None
    if programming_experience == "Experienced programmer new to Python":
        python_experience = prompt_with_choices(
            "What is your current Python experience?",
            ["No Python experience", "Basic Python knowledge"]
        )
    
    learning_goal = click.prompt("What is your learning goal for Python?", type=str)
    
    learning_style = prompt_with_choices(
        "What is your preferred learning style?",
        ["Hands-on projects", "Reading and theory-based learning"]
    )
    
    return UserInfo(
        programming_experience=programming_experience,
        python_experience=python_experience,
        learning_goal=learning_goal,
        learning_style=learning_style
    )
