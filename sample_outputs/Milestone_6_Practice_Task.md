# Practice Task

# Practice Task: Building a Complete Python Project

## Introduction
In this milestone task, you will apply all the concepts you've learned so far to build a complete Python project. This project will involve planning, designing, implementing features, and finally deploying your application. You will create a simple task management application that allows users to add, view, and delete tasks.

## Step-by-Step Instructions

### 1. Project Setup
- **Create a new project directory**: 
  - Name it `task_manager`.
  
- **Create the main Python script file**:
  - Inside the `task_manager` directory, create a file named `main.py`.

- **Additional files needed**:
  - Create a file named `tasks.txt` to store tasks persistently.
  - Optionally, create a `README.md` file to document your project.

### 2. Detailed Requirements
- **Functionality**:
  - The application should allow users to:
    - Add a new task (with a description).
    - View all tasks.
    - Delete a task by its number.
  
- **User Interface**:
  - Use a simple text-based menu to interact with the user.
  - The menu should display options to add, view, delete tasks, and exit the application.

- **Data Storage**:
  - Store tasks in `tasks.txt` in a simple format (one task per line).

### 3. Expected Output or Behavior
- When the application runs, it should display a menu like this:
  ```
  Task Manager
  1. Add Task
  2. View Tasks
  3. Delete Task
  4. Exit
  ```
- Users can select an option by entering the corresponding number.
- When adding a task, the user should be prompted to enter a task description.
- When viewing tasks, the application should list all tasks with their corresponding numbers.
- When deleting a task, the user should enter the number of the task to be deleted, and the application should confirm the deletion.

### 4. Hints or Tips for Completing the Task
- Use functions to organize your code. For example, create separate functions for adding, viewing, and deleting tasks.
- Use exception handling to manage errors, such as trying to delete a task that doesn't exist.
- Consider using a loop to keep the application running until the user chooses to exit.

### 5. Additional Resources
- [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

By completing this task, you will gain hands-on experience in building a complete project, reinforcing your understanding of Python programming concepts. Good luck!