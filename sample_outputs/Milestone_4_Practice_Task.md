# Concept Explanations and Practice Task

# File Handling and Modules: Practice Task

## 1. Concept Explanations

### File Operations
File operations in Python allow you to work with files on your filesystem. The basic operations include opening a file, reading from it, writing to it, and closing it. Python provides a built-in `open()` function that is used to open a file and return a file object. The file can be opened in different modes, such as:
- `'r'`: Read mode, which is the default.
- `'w'`: Write mode, which truncates the file to zero length.
- `'a'`: Append mode, which writes data at the end of the file.
- `'b'`: Binary mode, used for non-text files.

Example:
```python
# Opening a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
```

### Error Handling
Error handling in Python is managed using `try`, `except`, `else`, and `finally` blocks. This allows you to gracefully handle exceptions that may occur during execution, such as file not found errors or permission errors.

Example:
```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

### Modules and Packages
Modules are Python files that contain Python code, which can be functions, classes, or variables. Packages are a way of organizing related modules into a single directory hierarchy. Python's standard library includes many useful modules, such as `os`, `sys`, `json`, etc., which can be imported using the `import` statement.

Example:
```python
# Importing a module
import os

# Using a function from the os module
current_directory = os.getcwd()
print(current_directory)
```

### Real-world Applications
In real-world Python programming, file handling is essential for data persistence and interaction with the filesystem. Modules and packages help in organizing code and reusing functionality. Error handling ensures that your program can handle unexpected situations without crashing.

## 2. Practice Task

### a. Introduction to the Task
Create a simple command-line application that reads tasks from a file, allows the user to add new tasks, and saves the updated list back to the file. This task will help you practice file operations, error handling, and using Python's standard libraries.

### b. Step-by-step Instructions

1. **Set Up the Project**
   - Create a new directory for the project named `task_manager`.
   - Inside the `task_manager` directory, create a main Python script file named `task_manager.py`.

2. **Additional Files Needed**
   - `tasks.txt`: A text file that will store the list of tasks.

### c. Detailed Requirements

1. **Reading Tasks**
   - Implement functionality to read tasks from `tasks.txt`. If the file does not exist, handle the error gracefully and start with an empty task list.

2. **Adding New Tasks**
   - Allow the user to input a new task, which is added to the list and saved back to `tasks.txt`.

3. **Saving Tasks**
   - Ensure that the updated list of tasks is saved back to the file after each modification.

4. **User Interface**
   - The script should provide a simple menu to the user:
     - View all tasks
     - Add a new task
     - Exit the application

### d. Expected Output or Behavior
- When the script is run, it should display a menu.
- If the user chooses to view tasks, display the current list of tasks.
- If the user adds a task, it should be appended to the list and saved to the file.
- Handle any file-related errors gracefully.

### e. Hints or Tips
- Use the `with` statement for file operations to ensure files are properly closed.
- Use exception handling to manage errors such as file not found.
- Consider using Python's `os` module to check for file existence.

### f. Additional Resources
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Error Handling](https://docs.python.org/3/tutorial/errors.html)
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)