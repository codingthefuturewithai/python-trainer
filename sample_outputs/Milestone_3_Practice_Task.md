# Practice Task

# Practice Task: Organizing Code with Modules and Packages

## Introduction
In this practice task, you will explore how to organize your Python code using modules and packages. You will create a simple project that utilizes Python's standard library modules, such as `os`, `sys`, and `datetime`. By the end of this task, you will have a better understanding of how to structure your code and leverage the power of Python's built-in functionalities.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a new project directory**: Name it `my_project`.
- **Navigate into the project directory**: 
  ```bash
  cd my_project
  ```
- **Create the main Python script file**: Name it `main.py`.
- **Create a new directory for your package**: Name it `my_package`.
- **Inside `my_package`, create an empty file named `__init__.py`**: This file will allow Python to recognize the directory as a package.
- **Create an additional module file inside `my_package`**: Name it `utils.py`.

Your project structure should look like this:
```
my_project/
│
├── main.py
└── my_package/
    ├── __init__.py
    └── utils.py
```

### 2. Detailed Requirements
- **In `utils.py`**:
  - Create a function named `get_current_time()` that returns the current date and time as a formatted string (e.g., "YYYY-MM-DD HH:MM:SS").
  - Create a function named `list_directory_contents()` that returns a list of files and directories in the current working directory using the `os` module.

- **In `main.py`**:
  - Import the `get_current_time` and `list_directory_contents` functions from the `my_package.utils` module.
  - Call `get_current_time()` and print the result.
  - Call `list_directory_contents()` and print the list of files and directories.

### 3. Expected Output or Behavior
When you run `main.py`, you should see output similar to the following:
```
Current Time: 2023-10-01 12:34:56
Directory Contents: ['file1.txt', 'file2.py', 'my_package']
```
(Note: The actual current time and directory contents will vary based on your system.)

### 4. Hints or Tips for Completing the Task
- Use the `datetime` module to get the current date and time.
- Use `os.listdir()` to list the contents of the current directory.
- Make sure to handle any potential exceptions, such as when accessing the file system.

### 5. Additional Resources
- [Python Modules and Packages Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library Documentation](https://docs.python.org/3/library/index.html)
- [Working with Dates and Times in Python](https://realpython.com/python-datetime/)

By completing this task, you will gain hands-on experience with organizing your code into modules and packages, as well as utilizing Python's standard library effectively. Happy coding!