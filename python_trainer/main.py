import click
from python_trainer.config import UserInfo
from python_trainer.cli import gather_user_info
from python_trainer.prompt_generator import generate_prompt
from python_trainer.openai_utils import get_training_plan

def main():
    """Main entry point for the Python Trainer application."""
    click.echo("Welcome to the Python Trainer App!")
    user_info = gather_user_info()
    click.echo(f"User information collected: {user_info}")
    
    prompt = generate_prompt(user_info)
    click.echo("\nGenerating training plan...")
    
    training_plan = get_training_plan(prompt)
    click.echo("\nGenerated Training Plan:")
    click.echo(training_plan)

if __name__ == "__main__":
    main()
