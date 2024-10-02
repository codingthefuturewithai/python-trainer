# Practice Task

# Practice Task: Milestone 4 - Error Handling and Testing

## Introduction
In this practice task, you will create a simple Python application that performs basic arithmetic operations. You will implement exception handling to manage potential errors, and you will write unit tests to ensure your code functions correctly. This task will help you solidify your understanding of error handling and testing in Python.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a new project directory**: Name it `arithmetic_operations`.
- **Create the main Python script file**: Inside the `arithmetic_operations` directory, create a file named `calculator.py`.
- **Create an additional file for tests**: In the same directory, create a file named `test_calculator.py`.

### 2. Detailed Requirements for the Task
- In `calculator.py`, implement a simple calculator class with the following methods:
  - `add(a, b)`: Returns the sum of `a` and `b`.
  - `subtract(a, b)`: Returns the difference of `a` and `b`.
  - `multiply(a, b)`: Returns the product of `a` and `b`.
  - `divide(a, b)`: Returns the quotient of `a` and `b`. If `b` is zero, raise a `ValueError` with the message "Cannot divide by zero".
  
- Implement exception handling using `try` and `except` blocks to catch and handle errors gracefully.
  
- In `test_calculator.py`, write unit tests using the `unittest` framework to test the following:
  - Test that the `add`, `subtract`, and `multiply` methods return the correct results.
  - Test that the `divide` method raises a `ValueError` when attempting to divide by zero.
  
### 3. Expected Output or Behavior
- When running the `calculator.py` script, it should not produce any output directly. Instead, it should handle any exceptions that occur during method calls.
- When running the tests in `test_calculator.py` using the command `python -m unittest test_calculator.py`, you should see output indicating whether the tests passed or failed.

### 4. Hints or Tips for Completing the Task
- Use `try` and `except` blocks around your method calls in `calculator.py` to catch exceptions.
- Use `assertEqual` in your unit tests to compare the expected output with the actual output.
- Remember to import the `unittest` module at the beginning of your `test_calculator.py` file.
- You can run your tests from the command line to see the results.

### 5. Additional Resources
- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [Real Python - Unit Testing in Python](https://realpython.com/python-testing/)
- [Python Official Documentation](https://docs.python.org/3/)

By completing this task, you will gain practical experience in managing exceptions and writing tests, which are essential skills for any Python developer. Good luck!