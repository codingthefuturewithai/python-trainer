# Concept Explanations and Practice Task

# Control Flow and Functions: Practice Task

## 1. Concept Explanations

### Conditional Statements
Conditional statements allow you to execute specific blocks of code based on certain conditions. The primary conditional statements in Python are `if`, `elif`, and `else`. They are used to make decisions in your code.

Example:
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

**Real-world use:** Conditional statements are used in applications to handle different user inputs or scenarios, such as determining access rights based on user roles.

### Loops
Loops are used to execute a block of code repeatedly. Python provides `for` loops and `while` loops.

Example of a `for` loop:
```python
for i in range(5):
    print("Iteration", i)
```

Example of a `while` loop:
```python
count = 0
while count < 5:
    print("Count is", count)
    count += 1
```

**Real-world use:** Loops are used for tasks that require repetition, such as processing items in a list or reading lines from a file.

### Functions
Functions allow you to encapsulate reusable code blocks, making your code modular and organized. You define a function using the `def` keyword.

Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

**Real-world use:** Functions are used to perform specific tasks, such as data validation or calculations, and can be reused across different parts of a program.

### Scope and Lifetime of Variables
Scope refers to the visibility of variables in different parts of your code. Variables defined inside a function are local to that function, while variables defined outside are global.

Example:
```python
def my_function():
    local_var = "I'm local"
    print(local_var)

global_var = "I'm global"
my_function()
print(global_var)
```

**Real-world use:** Understanding variable scope helps prevent errors related to variable access and modification, especially in larger codebases.

## 2. Practice Task

### a. Task Introduction
Create a simple command-line Python application that simulates a basic calculator. This task will help you practice using control flow statements and functions to build a reusable, modular application.

### b. Project Setup Instructions
- **Create a new project directory** called `simple_calculator`.
- **Main Python script file:** `calculator.py`
- **No additional files are needed**.

### c. Detailed Requirements
1. **Create a function** for each arithmetic operation: addition, subtraction, multiplication, and division.
   - Each function should take two arguments and return the result.
2. **Implement a loop** that allows the user to perform multiple calculations until they choose to exit.
3. **Use conditional statements** to determine which operation to perform based on user input.
4. **Handle division by zero** by displaying an appropriate error message instead of crashing.

### d. Expected Output or Behavior
- The program should display a menu with options for addition, subtraction, multiplication, division, and exit.
- After choosing an operation, the user should be prompted to enter two numbers.
- The program should display the result of the operation and return to the menu.
- If the user attempts to divide by zero, an error message should be displayed, and the menu should be shown again.
- The program should continue running until the user selects the exit option.

### e. Hints or Tips for Completing the Task
- Use a `while` loop to keep the program running until the user decides to exit.
- Use `input()` to collect user input and `int()` or `float()` to convert it to a number.
- Organize your functions at the top of the file and call them inside your loop based on user input.

### f. Additional Resources
- [Python Official Documentation on Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Real Python: Python Conditional Statements](https://realpython.com/python-conditional-statements/)
- [W3Schools: Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)

This practice task will not only solidify your understanding of control flow and functions but also demonstrate how these concepts are applied in building a simple, interactive Python application.