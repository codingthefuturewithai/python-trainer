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
    the training plan. It includes the milestone name, objective, 
    and associated topics.

    Args:
        training_plan (TrainingPlan): The training plan containing 
        milestones and their respective details.

    Returns:
        str: A string formatted in Markdown for the training plan.
    """
    formatted = "# Python Training Plan\n\n"
    for milestone in training_plan.milestones:
        formatted += f"## {milestone.name}\n\n"
        formatted += f"**Objective:** {milestone.objective}\n\n"
        formatted += "**Topics:**\n"
        for topic in milestone.topics:
            formatted += f"- {topic}\n"
        formatted += "\n"
    return formatted

def main():
    """Main entry point for the Python Trainer application."""
    click.echo("Welcome to the Python Trainer App!")
    
    output_dir = create_output_directory()
    click.echo(f"All files will be saved in: {output_dir}")
    
    user_info = gather_user_info()
    click.echo(f"User information collected: {user_info}")
    
    prompt = generate_prompt(user_info)
    click.echo("\nGenerating training plan...")
    
    training_plan = get_training_plan(prompt)
    if not training_plan:
        click.echo("Error: Training plan generation failed. Please try again.")
        return

    # click.echo("\nGenerated Training Plan:")
    # click.echo(training_plan)
    
    # Convert TrainingPlan to a formatted string
    formatted_plan = format_training_plan(training_plan)
    
    # Save the training plan to a Markdown file
    save_path = save_training_plan(formatted_plan, filename="training_plan.md")
    click.echo(f"\nTraining plan successfully saved as Markdown to {save_path}")

    # Prompt user to generate practice task for the first milestone
    generate_task = prompt_yes_no("Would you like to generate the practice task for the first milestone?")
    if generate_task:
        click.echo("Generating practice task for the first milestone...")
        # Extract the first milestone's details from the TrainingPlan object
        if training_plan.milestones:
            first_milestone = training_plan.milestones[0]
            click.echo(f"First Milestone: {first_milestone}")
            task_prompt = generate_task_prompt(first_milestone.dict())
        else:
            click.echo("Error: No milestones found in the training plan.")
            return
        task = get_practice_task(task_prompt)
        click.echo("\nGenerated Practice Task for the First Milestone:")
        click.echo(task)
        # Save the practice task to a Markdown file
        task_save_path = save_training_plan(task, filename="Milestone_1_Practice_Task.md")
        click.echo(f"\nPractice task successfully saved as Markdown to {task_save_path}")
    else:
        click.echo("You can generate the practice task later by running this command again.")
    
    # Prompt user to generate practice tasks for all remaining milestones
    generate_all_tasks = prompt_yes_no("Would you like to generate practice tasks for all remaining milestones? (yes/no)")
    if generate_all_tasks:
        click.echo("Generating practice tasks for all remaining milestones...")
        for i, milestone in enumerate(training_plan.milestones[1:], start=2):  # Start from the second milestone
            click.echo(f"Generating practice task for Milestone {i}...")
            task_prompt = generate_task_prompt(milestone.dict())
            task = get_practice_task(task_prompt)
            task_save_path = save_practice_task(task, i)
            click.echo(f"Practice task for Milestone {i} saved to {task_save_path}")
        click.echo("All practice tasks have been generated and saved.")
    else:
        click.echo("You can generate practice tasks for the remaining milestones later by running this command again.")

    click.echo("Thank you for using the Python Trainer App!")

if __name__ == "__main__":
    main()
