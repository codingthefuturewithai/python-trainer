import click
import json
from python_trainer.config import UserInfo
from python_trainer.cli import gather_user_info, prompt_yes_no
from python_trainer.prompt_generator import generate_prompt, generate_task_prompt
from python_trainer.openai_utils import get_training_plan, get_practice_task
from python_trainer.utils.file_utils import save_training_plan, save_practice_task, create_output_directory

def format_training_plan(training_plan):
    """
    Formats the given training plan into a Markdown string.

    This function takes a TrainingPlan object and constructs a 
    Markdown-formatted string that details each milestone within 
    the training plan. It includes the background information,
    milestone name, objective, and associated topics.

    Args:
        training_plan (TrainingPlan): The training plan containing 
        background information and milestones with their respective details.

    Returns:
        str: A string formatted in Markdown for the training plan.
    """
    formatted = "# Python Training Plan\n\n"
    
    # Add background information
    formatted += "## Background\n\n"
    formatted += f"{training_plan.background}\n\n"
    
    formatted += "## Milestones\n\n"
    for milestone in training_plan.milestones:
        formatted += f"### {milestone.name}\n\n"
        formatted += f"**Objective:** {milestone.objective}\n\n"
        formatted += "**Topics:**\n"
        for topic in milestone.topics:
            formatted += f"- {topic}\n"
        formatted += "\n"
    return formatted

def main():
    """Main entry point for the Python Trainer application."""
    click.echo("\n" + "=" * 50)
    click.echo("Welcome to the Python Trainer App!".center(50))
    click.echo("=" * 50 + "\n")
    
    output_dir = create_output_directory()
    click.echo(f"All files will be saved in:\n{output_dir}\n")
    
    click.echo("-" * 50)
    click.echo("User Information".center(50))
    click.echo("-" * 50 + "\n")
    user_info = gather_user_info()
    click.echo(f"\nUser information collected:\n{user_info}\n")
    
    click.echo("-" * 50)
    click.echo("Generating Training Plan".center(50))
    click.echo("-" * 50 + "\n")
    prompt = generate_prompt(user_info)
    click.echo("Generating training plan...\n")
    
    training_plan = get_training_plan(prompt)
    if not training_plan:
        click.echo("Error: Training plan generation failed. Please try again.")
        return

    formatted_plan = format_training_plan(training_plan)
    save_path = save_training_plan(formatted_plan, filename="training_plan.md")
    click.echo(f"Training plan successfully saved as Markdown to:\n{save_path}\n")

    click.echo("-" * 50)
    click.echo("Practice Tasks".center(50))
    click.echo("-" * 50 + "\n")
    generate_task = prompt_yes_no("Would you like to generate the practice task for the first milestone?")
    if generate_task:
        click.echo("\nGenerating practice task for the first milestone...\n")
        if training_plan.milestones:
            first_milestone = training_plan.milestones[0]
            click.echo(f"First Milestone: {first_milestone.name}\n")
            task_prompt = generate_task_prompt(first_milestone.dict(), user_info, training_plan)
        else:
            click.echo("Error: No milestones found in the training plan.")
            return
        task = get_practice_task(task_prompt)
        task_save_path = save_training_plan(task, filename="Milestone_1_Practice_Task.md")
        click.echo(f"Practice task successfully saved as Markdown to:\n{task_save_path}\n")
        
        click.echo("To get started with the practice task:")
        click.echo("1. Open the saved practice task file.")
        click.echo("2. Follow the step-by-step instructions to set up your project.")
        click.echo("3. Complete the task requirements as specified.")
        click.echo("4. Use the hints and resources provided if you get stuck.")
        click.echo("5. Compare your solution with the expected output.\n")
    else:
        click.echo("You can generate the practice task later by running this command again.\n")
    
    generate_all_tasks = prompt_yes_no("Would you like to generate practice tasks for all remaining milestones?")
    if generate_all_tasks:
        click.echo("\nGenerating practice tasks for all remaining milestones...\n")
        for i, milestone in enumerate(training_plan.milestones[1:], start=2):
            click.echo(f"Generating practice task for Milestone {i}...")
            task_prompt = generate_task_prompt(milestone.dict(), user_info, training_plan)
            task = get_practice_task(task_prompt)
            task_save_path = save_practice_task(task, i)
            click.echo(f"Practice task for Milestone {i} saved to:\n{task_save_path}\n")
        click.echo("All practice tasks have been generated and saved.\n")
    else:
        click.echo("You can generate practice tasks for the remaining milestones later by running this command again.\n")

    click.echo("=" * 50)
    click.echo("Thank you for using the Python Trainer App!".center(50))
    click.echo("=" * 50 + "\n")

if __name__ == "__main__":
    main()
