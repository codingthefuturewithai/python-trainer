import click
from python_trainer.config import UserInfo
from python_trainer.cli import gather_user_info, prompt_yes_no
from python_trainer.prompt_generator import generate_prompt
from python_trainer.openai_utils import get_training_plan
from python_trainer.utils.file_utils import save_training_plan

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
    
    # Save the training plan to a Markdown file
    save_path = save_training_plan(training_plan)
    click.echo(f"\nTraining plan successfully saved as Markdown to {save_path}")

    # Prompt user to generate practice task for the first milestone
    generate_task = prompt_yes_no("Would you like to generate the practice task for the first milestone?")
    if generate_task:
        click.echo("Generating practice task for the first milestone...")
        # TODO: Implement practice task generation
        click.echo("Practice task generation is not yet implemented. This feature will be available in a future update.")
    else:
        click.echo("You can generate the practice task later by running this command again.")
    
    click.echo("Thank you for using the Python Trainer App!")

if __name__ == "__main__":
    main()
