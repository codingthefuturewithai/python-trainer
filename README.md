# Python Trainer App

## Project Overview

The Python Trainer App is a command-line tool designed to create personalized Python training plans and practice tasks. It uses OpenAI's GPT model to generate custom learning content based on the user's experience level, learning goals, and preferred learning style. This tool is perfect for beginners starting their Python journey or experienced programmers looking to enhance their Python skills.

## Core Technologies

1. **Python**: The primary programming language used for the project.
2. **Click**: A Python package for creating beautiful command-line interfaces.
3. **Pydantic**: Used for data validation and settings management using Python type annotations.
4. **OpenAI API**: Leveraged to generate personalized training plans and practice tasks.
5. **python-dotenv**: Used for managing environment variables.

## Core Components

1. **main.py**: The entry point of the application, orchestrating the flow of the program.
2. **cli.py**: Handles command-line interface interactions and user input collection.
3. **config.py**: Defines the UserInfo model using Pydantic for structured user data.
4. **prompt_generator.py**: Generates prompts for the OpenAI API based on user information.
5. **openai_utils.py**: Manages interactions with the OpenAI API, including sending requests and parsing responses.
6. **schemas.py**: Defines Pydantic models for the training plan structure.
7. **utils/file_utils.py**: Handles file operations, such as saving the training plan to a file.

## How to Build and Run

1. Clone the repository:
   ```
   git clone https://github.com/codingthefuturewithai/python-trainer.git
   cd python-trainer-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Copy the `.env_example` file to create a new `.env` file in the project root directory:
     ```
     cp .env_example .env
     ```
   - Open the `.env` file and replace `your_api_key_here` with your actual OpenAI API key:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

5. Run the application:
   ```
   python -m python_trainer.main
   ```

6. Follow the prompts to input your information and generate a personalized Python training plan.

## Usage

When you run the application, it will:
1. Prompt you for information about your programming experience, learning goals, and preferred learning style.
2. Generate a personalized Python training plan using the OpenAI API.
3. Save the training plan as a Markdown file.
4. Offer to generate a practice task for the first milestone.
5. If requested, generate and save the practice task as a separate Markdown file.

The generated training plan and practice task will be saved in the current working directory as `training_plan.md` and `Milestone_1_Practice_Task.md` respectively.

## Example Output

After running the application, you'll find two new files in your current directory:

1. `training_plan.md`: Contains the personalized Python training plan with multiple milestones.
2. `Milestone_1_Practice_Task.md`: Contains a practice task for the first milestone (if you chose to generate it).

These files will be in Markdown format, making them easy to read and share.

## Contributing

Contributions to the Python Trainer App are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Future Work

The Python Trainer App has several exciting possibilities for future enhancements:

1. **Dynamic Knowledge Assessment**: Implement a short, adaptive quiz to evaluate the user's Python knowledge level. This assessment would be used to further customize and adapt the training plan.

2. **Integrated Development Environment**: Add the ability to launch a development container for users to execute their Python practice tasks directly within the application. This would provide a consistent and controlled environment for all learners.

3. **Task Evaluation**: Develop functionality for the trainer to evaluate the learner's completed tasks. This could include automated code review, style checking, and performance analysis.

4. **Adaptive Learning**: Implement the ability for the trainer to dynamically adapt the training plan based on:
   - The learner's perceived progress
   - The learner's pace of learning
   - Specific requests or redirections from the student

5. **Progress Tracking**: Create a system to track and visualize the learner's progress over time, providing motivation and insights into areas that may need more focus.

6. **Web-based User Interface**: Create a UI to allow the user to generate a plan and exercises, update the plan, track progress, etc.

These enhancements would make the Python Trainer App an even more powerful and personalized learning tool, adapting to each user's unique learning journey.
