# Concept Explanations and Practice Task

# Introduction to Python: Practice Task

## 1. Concept Explanations

### Python Setup
To start programming in Python, you need to have Python installed on your machine. The Python interpreter can be downloaded from [python.org](https://www.python.org/downloads/). Once installed, Python scripts can be executed in a terminal (command line) or through an integrated development environment (IDE) like PyCharm, VSCode, or Jupyter Notebook.

### Basic Syntax
Python's syntax is designed to be readable and straightforward. Key points include:

- **Indentation**: Python uses indentation to define code blocks instead of curly braces or keywords. Consistent indentation (usually 4 spaces) is crucial.
- **Comments**: Use `#` for single-line comments and `'''` or `"""` for multi-line comments.
  
Example:
```python
# This is a single-line comment

def greet():
    """This is a multi-line comment
    explaining the greet function"""
    print("Hello, World!")
```

### Variables and Data Types
Python is dynamically typed, meaning you don't need to declare variable types. Basic data types include:

- **Integers** (`int`): Whole numbers, e.g., `a = 5`
- **Floating-point numbers** (`float`): Decimal numbers, e.g., `b = 3.14`
- **Strings** (`str`): Text, e.g., `c = "Hello"`
- **Booleans** (`bool`): True or False values, e.g., `d = True`

Example:
```python
name = "Alice"
age = 30
height = 5.5
is_student = False
```

### Input and Output
Python can read input from the user and display output to the console using the `input()` and `print()` functions, respectively.

Example:
```python
user_name = input("Enter your name: ")
print("Hello, " + user_name)
```

### Real-World Application
These concepts form the foundation for any Python program. You'll use variables and data types to store and manipulate data, and input/output functions to interact with users. Understanding basic syntax is essential to writing clear and error-free Python code.

## 2. Practice Task

### a. Introduction to the Task
For this task, you'll create a simple program that asks the user for their name and age, then calculates and displays the year they will turn 100. This exercise will help you practice setting up a Python environment, understanding basic syntax, using variables, and handling input/output.

### b. Step-by-Step Instructions

#### Project Setup
1. **Create a New Project**: Set up a new directory for your project.
2. **Main Python Script File**: Create a file named `age_calculator.py` in your project directory.

#### Additional Files
- No additional files are needed for this task.

### c. Detailed Requirements
1. Prompt the user to enter their name.
2. Ask the user to enter their current age.
3. Calculate the year when the user will turn 100 years old.
4. Print a message to the user with the calculated year.

### d. Expected Output or Behavior
When the user inputs their name and age, the program should output a message like:
```
Enter your name: Alice
Enter your age: 30
Hello Alice, you will turn 100 years old in the year 2093.
```

### e. Hints or Tips
- Use the `input()` function to gather input from the user.
- Remember that `input()` returns a string, so you'll need to convert the age to an integer using `int()`.
- Use the current year to calculate the year the user will turn 100. You can hard-code the current year or use the `datetime` module to retrieve it dynamically.

### f. Additional Resources
- [Official Python Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.learnpython.org/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

By completing this task, you'll gain hands-on experience with Python's basic syntax, variables, and input/output operations, setting a solid foundation for more complex projects.