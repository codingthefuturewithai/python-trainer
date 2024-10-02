# Practice Task

# Practice Task: Milestone 2 - Data Structures and File Handling

## Introduction
In this practice task, you will create a simple contact management system that utilizes Python's built-in data structures and file handling capabilities. You will learn how to store, retrieve, and manipulate contact information using lists, dictionaries, and sets, while also practicing reading from and writing to files.

## Project Setup Instructions

1. **Create a New Project**: 
   - Open your preferred code editor or IDE (e.g., VSCode, PyCharm).
   - Create a new folder for your project named `contact_manager`.

2. **Name the Main Python Script File**: 
   - Inside the `contact_manager` folder, create a new Python file named `main.py`.

3. **Additional Files Needed**: 
   - Create a text file named `contacts.txt` in the same folder. This file will be used to store the contact information.

## Detailed Requirements for the Task

1. **Functionality**:
   - The program should allow users to:
     - Add a new contact (name, phone number, email).
     - View all contacts.
     - Search for a contact by name.
     - Delete a contact by name.
     - Save contacts to `contacts.txt` and load them from this file when the program starts.

2. **Data Structures**:
   - Use a list to store contacts.
   - Each contact should be represented as a dictionary with keys: `name`, `phone`, and `email`.
   - Use a set to ensure that contact names are unique.

3. **File Handling**:
   - Implement functions to read from and write to `contacts.txt`.
   - When writing to the file, save each contact on a new line in the format: `name,phone,email`.
   - When reading from the file, load the contacts into the list and set.

## Expected Output or Behavior

- When the program runs, it should display a menu with options to add, view, search, delete contacts, and exit.
- After performing any operation, the program should return to the menu.
- Upon exiting, the program should save all contacts to `contacts.txt`.
- If the program is run again, it should load existing contacts from `contacts.txt`.

## Hints or Tips for Completing the Task

- Use `input()` to gather user input for adding and searching contacts.
- Use a loop to display the menu and handle user choices.
- Remember to handle cases where a contact might not be found when searching or deleting.
- Use exception handling when reading from or writing to files to manage potential errors (e.g., file not found).
- Consider using list comprehensions for filtering contacts.

## Additional Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python Dictionaries Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

By completing this task, you will gain practical experience with data structures and file handling in Python, which are essential skills for any programmer. Happy coding!