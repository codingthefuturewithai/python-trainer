import click
from python_trainer.config import UserInfo

def prompt_with_choices(text, choices):
    return click.prompt(
        text,
        type=click.Choice(choices),
        show_choices=False,
        prompt_suffix='\n' + '\n'.join(f'{i+1}) {choice}' for i, choice in enumerate(choices)) + '\nEnter the number of your choice: '
    )

def gather_user_info() -> UserInfo:
    """Gather user information through CLI prompts."""
    programming_experience = prompt_with_choices(
        "What is your programming experience?",
        ["No programming experience", "Experienced programmer new to Python"]
    )
    
    python_experience = prompt_with_choices(
        "What is your current Python experience?",
        ["Novice", "Beginner"]
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
