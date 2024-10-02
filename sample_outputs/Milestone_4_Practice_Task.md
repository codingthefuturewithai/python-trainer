# Practice Task

# Practice Task: File Handling and Exception Management

## Introduction
In this practice task, you will develop a Python script that demonstrates your ability to read from and write to various file formats, including text, CSV, and JSON files. You will also implement exception handling to manage potential errors that may arise during file operations. This task will help solidify your understanding of file handling and exception management in Python.

## Project Setup Instructions

1. **Create a New Project**: 
   - Create a new directory for your project. You can name it `file_handling_practice`.

2. **Main Python Script File**: 
   - Inside the `file_handling_practice` directory, create a new Python file named `file_manager.py`.

3. **Additional Files Needed**: 
   - Create a text file named `sample.txt` with the following content:
     ```
     Hello, World!
     This is a sample text file.
     ```
   - Create a CSV file named `data.csv` with the following content:
     ```
     Name,Age,Occupation
     Alice,30,Engineer
     Bob,25,Designer
     Charlie,35,Teacher
     ```
   - Create a JSON file named `data.json` with the following content:
     ```json
     {
       "employees": [
         {"name": "Alice", "age": 30, "occupation": "Engineer"},
         {"name": "Bob", "age": 25, "occupation": "Designer"},
         {"name": "Charlie", "age": 35, "occupation": "Teacher"}
       ]
     }
     ```

## Detailed Requirements for the Task

1. **Reading from Files**:
   - Read the content of `sample.txt` and print it to the console.
   - Read the `data.csv` file and print each row as a dictionary.
   - Read the `data.json` file and print the list of employees.

2. **Writing to Files**:
   - Create a new text file named `output.txt` and write the following content to it:
     ```
     This is an output file.
     It contains results from the file handling task.
     ```
   - Append a new line to `output.txt` that states how many employees were read from the JSON file.

3. **Exception Handling**:
   - Implement exception handling for all file operations. Use `try`, `except`, and `finally` blocks to handle potential errors (e.g., file not found, permission errors).
   - Ensure that any opened files are properly closed in the `finally` block.

## Expected Output or Behavior

- When you run `file_manager.py`, you should see the content of `sample.txt`, the rows from `data.csv` printed as dictionaries, and the list of employees from `data.json` printed to the console.
- The `output.txt` file should be created with the specified content, and it should include the count of employees at the end.

## Hints or Tips for Completing the Task

- Use the built-in `open()` function to handle file operations.
- For reading CSV files, consider using the `csv` module.
- For reading JSON files, use the `json` module.
- Remember to handle exceptions gracefully to avoid crashing your program.

## Additional Resources

- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Python JSON Module Documentation](https://docs.python.org/3/library/json.html)
- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)

Good luck with your task! Happy coding!