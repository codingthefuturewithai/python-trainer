import click
from python_trainer.config import UserInfo
from python_trainer.cli import gather_user_info

def main():
    """Main entry point for the Python Trainer application."""
    click.echo("Welcome to the Python Trainer App!")
    user_info = gather_user_info()
    click.echo(f"User information collected: {user_info}")
    # TODO: Use this information to generate a training plan

if __name__ == "__main__":
    main()
