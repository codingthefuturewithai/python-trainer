### Practice Task for Milestone 1: Introduction to Python

#### Task Overview
In this practice task, you will familiarize yourself with the basics of Python syntax, set up your Python environment, and run your first Python script. You will also learn how to use comments and documentation in your code.

#### Instructions

1. **Setting Up Your Python Environment**
   - If you haven't already, download and install Python from the official website: [python.org](https://www.python.org/downloads/).
   - Verify your installation by opening a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and typing:
     ```bash
     python --version
     ```
   - You should see the version of Python you installed. If you see an error, please troubleshoot your installation.

2. **Creating Your First Python Script**
   - Open a text editor (like Notepad, VSCode, or PyCharm) and create a new file named `hello_world.py`.
   - In this file, write the following code:
     ```python
     # This is my first Python script
     print("Hello, World!")
     ```
   - Save the file.

3. **Running Your Python Script**
   - Open your terminal and navigate to the directory where you saved `hello_world.py`. You can use the `cd` command to change directories. For example:
     ```bash
     cd path/to/your/directory
     ```
   - Run your script by typing:
     ```bash
     python hello_world.py
     ```
   - **Expected Output:**
     ```
     Hello, World!
     ```

4. **Understanding Basic Syntax and Indentation**
   - Modify your script to include a simple calculation and print the result. Update your `hello_world.py` file to look like this:
     ```python
     # This is my first Python script
     print("Hello, World!")

     # Performing a simple calculation
     a = 5
     b = 10
     sum = a + b
     print("The sum of", a, "and", b, "is:", sum)
     ```
   - Run the script again. 
   - **Expected Output:**
     ```
     Hello, World!
     The sum of 5 and 10 is: 15
     ```

5. **Using Comments and Documentation**
   - Add comments to your code to explain what each part does. Your updated script should look like this:
     ```python
     # This is my first Python script
     print("Hello, World!")  # Print a greeting

     # Performing a simple calculation
     a = 5  # First number
     b = 10  # Second number
     sum = a + b  # Calculate the sum
     print("The sum of", a, "and", b, "is:", sum)  # Print the result
     ```
   - Run the script again to ensure it still works correctly.

6. **Exploring Python Documentation**
   - Visit the official Python documentation at [docs.python.org](https://docs.python.org/3/).
   - Read the introductory section to understand more about Python's features and capabilities.

#### Hints
- If you encounter any errors while running your script, carefully check for typos or indentation issues. Python is sensitive to indentation.
- Use `#` to add comments in your code. Comments are ignored by the Python interpreter and are useful for explaining your code to others (or yourself in the future).

#### Submission
- Once you have completed the task, ensure your `hello_world.py` file is saved with all the modifications.
- You can take a screenshot of your terminal showing the output of your script and submit it as proof of completion.

Good luck, and enjoy your journey into the world of Python programming!