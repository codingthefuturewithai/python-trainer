# Concept Explanations and Practice Task

**Python Foundations for AI and ML: Practice Task**
=====================================================

**Concept Explanations**
------------------------

Before diving into the practice task, let's review some key concepts related to advanced Python data structures, file operations, and object-oriented programming.

### Advanced Python Data Structures

*   **NumPy Arrays**: NumPy arrays are a fundamental data structure in Python for scientific computing. They are similar to lists but offer more efficient storage and operations for numerical data.

    Example:
    ```python
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform operations on the array
print(arr.mean())  # Output: 3.0
print(arr.std())   # Output: 1.4142135623730951
```
*   **Pandas DataFrames**: Pandas DataFrames are a powerful data structure for working with tabular data. They offer efficient data manipulation, filtering, and grouping capabilities.

    Example:
    ```python
import pandas as pd

# Create a Pandas DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Perform operations on the DataFrame
print(df.mean())  # Output: Age    29.75
print(df.groupby('Age').count())  # Output: Age  24  1 28  1 32  1 35  1
```

### File Operations and Data Loading

*   **CSV Files**: CSV (Comma Separated Values) files are a common format for storing tabular data. Pandas provides an efficient way to read and write CSV files.

    Example:
    ```python
import pandas as pd

# Read a CSV file
df = pd.read_csv('data.csv')

# Write to a CSV file
df.to_csv('output.csv', index=False)
```
*   **JSON Files**: JSON (JavaScript Object Notation) files are a lightweight format for storing data. Python's built-in `json` module provides an easy way to read and write JSON files.

    Example:
    ```python
import json

# Read a JSON file
with open('data.json') as f:
    data = json.load(f)

# Write to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f)
```

### Object-Oriented Programming in Python

*   **Classes and Objects**: Classes define a blueprint for creating objects, which are instances of the class. Objects have attributes (data) and methods (functions).

    Example:
    ```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Create an object
person = Person("John", 30)

# Call a method on the object
person.greet()  # Output: Hello, my name is John and I'm 30 years old.
```

**Practice Task**
-----------------

### Introduction

In this practice task, you'll create a Python script that demonstrates your understanding of advanced Python data structures, file operations, and object-oriented programming. You'll work with a simple dataset of books, storing and retrieving data from CSV and JSON files using Pandas and Python's built-in `json` module.

### Step-by-Step Instructions

1.  Create a new project folder and navigate to it in your terminal or command prompt.
2.  Create a new Python script file called `book_manager.py`.
3.  Create two additional files: `books.csv` and `books.json`. These will store the book data in CSV and JSON formats, respectively.

### Detailed Requirements

Your `book_manager.py` script should:

1.  Define a `Book` class with attributes for `title`, `author`, and `year`. The class should have methods for `__init__` (initialization), `__str__` (string representation), and `to_dict` (converting the book to a dictionary).
2.  Create a `BookManager` class that handles book data storage and retrieval. The class should have methods for:
    *   `load_csv`: Load book data from the `books.csv` file using Pandas.
    *   `save_csv`: Save book data to the `books.csv` file using Pandas.
    *   `load_json`: Load book data from the `books.json` file using Python's built-in `json` module.
    *   `save_json`: Save book data to the `books.json` file using Python's built-in `json` module.
    *   `add_book`: Add a new book to the dataset.
    *   `remove_book`: Remove a book from the dataset by its title.
    *   `get_books`: Return a list of all books in the dataset.
3.  In the `book_manager.py` script, create an instance of the `BookManager` class and demonstrate its methods by:
    *   Loading book data from the `books.csv` file.
    *   Adding a new book to the dataset.
    *   Saving the updated dataset to the `books.json` file.
    *   Loading the book data from the `books.json` file.
    *   Removing a book from the dataset.
    *   Saving the updated dataset to the `books.csv` file.

### Expected Output or Behavior

Your script should output the book data in a readable format after each operation, demonstrating the successful loading, adding, removing, and saving of book data.

### Hints or Tips

*   Use Pandas to efficiently handle CSV data.
*   Use Python's built-in `json` module to handle JSON data.
*   Implement error handling to ensure your script can handle missing files or invalid data.
*   Use Markdown formatting to make your code more readable.

### Additional Resources

*   [Pandas Documentation](https://pandas.pydata.org/docs/)
*   [Python `json` Module Documentation](https://docs.python.org/3/library/json.html)
*   [Python Object-Oriented Programming Tutorial](https://docs.python.org/3/tutorial/classes.html)

By completing this practice task, you'll demonstrate your understanding of advanced Python data structures, file operations, and object-oriented programming, preparing you for more complex tasks in AI and ML with Python.