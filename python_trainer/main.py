import click
from python_trainer.config import UserInfo
from python_trainer.cli import gather_user_info
from python_trainer.prompt_generator import generate_prompt

def main():
    """Main entry point for the Python Trainer application."""
    click.echo("Welcome to the Python Trainer App!")
    user_info = gather_user_info()
    click.echo(f"User information collected: {user_info}")
    
    prompt = generate_prompt(user_info)
    click.echo("\nGenerated prompt for OpenAI GPT:")
    click.echo(prompt)
    
    # TODO: Send this prompt to OpenAI GPT and process the response

if __name__ == "__main__":
    main()
