import click
from python_trainer.config import UserInfo

def gather_user_info() -> UserInfo:
    """Gather user information through CLI prompts."""
    programming_experience = click.prompt(
        "What is your programming experience?",
        type=click.Choice(["No programming experience", "Experienced programmer new to Python"])
    )
    
    python_experience = click.prompt(
        "What is your current Python experience?",
        type=click.Choice(["Novice", "Beginner"])
    )
    
    learning_goal = click.prompt("What is your learning goal for Python?", type=str)
    
    learning_style = click.prompt(
        "What is your preferred learning style?",
        type=click.Choice(["Hands-on projects", "Reading and theory-based learning"])
    )
    
    return UserInfo(
        programming_experience=programming_experience,
        python_experience=python_experience,
        learning_goal=learning_goal,
        learning_style=learning_style
    )
