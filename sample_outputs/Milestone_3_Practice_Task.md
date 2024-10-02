# Practice Task

# Practice Task: Object-Oriented Programming in Python

## Introduction
In this practice task, you will create a simple library management system using Object-Oriented Programming (OOP) principles in Python. This task will help you understand how to define classes and objects, implement inheritance and polymorphism, and utilize encapsulation and abstraction in your code.

## Project Setup Instructions

1. **Create a New Project**: 
   - Create a new directory for your project called `library_management_system`.

2. **Name the Main Python Script File**: 
   - Inside the `library_management_system` directory, create a file named `main.py`.

3. **Additional Files Needed**: 
   - You will also create a file named `library.py` to define your classes.

## Detailed Requirements

1. **Define Classes**:
   - Create a base class called `Book` with the following attributes:
     - `title` (string)
     - `author` (string)
     - `isbn` (string)
     - `available` (boolean, default to `True`)
   - Implement methods in the `Book` class:
     - `__str__`: to return a string representation of the book.
     - `borrow`: to change the `available` status to `False`.
     - `return_book`: to change the `available` status to `True`.

2. **Create a Derived Class**:
   - Create a derived class called `EBook` that inherits from `Book` and adds the following attribute:
     - `file_size` (float, in MB)
   - Override the `__str__` method to include the `file_size`.

3. **Implement a Library Class**:
   - Create a class called `Library` that contains:
     - A list to hold `Book` and `EBook` objects.
     - Methods to:
       - `add_book(book)`: to add a book to the library.
       - `borrow_book(isbn)`: to borrow a book by its ISBN.
       - `return_book(isbn)`: to return a book by its ISBN.
       - `list_books()`: to print all books in the library.

4. **Main Functionality**:
   - In `main.py`, create an instance of `Library`.
   - Add at least two `Book` objects and two `EBook` objects to the library.
   - Demonstrate borrowing and returning books, and list all books in the library.

## Expected Output or Behavior
When you run `main.py`, you should see output similar to the following:

```
Books in the library:
Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 1234567890, Available: True
Title: 1984, Author: George Orwell, ISBN: 0987654321, Available: True
Title: Python Programming, Author: John Doe, ISBN: 1122334455, Available: True, File Size: 1.5 MB
Title: Data Science 101, Author: Jane Smith, ISBN: 5544332211, Available: True, File Size: 2.0 MB

Borrowing '1984'...
Book borrowed successfully.

Books in the library after borrowing:
Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 1234567890, Available: True
Title: 1984, Author: George Orwell, ISBN: 0987654321, Available: False
Title: Python Programming, Author: John Doe, ISBN: 1122334455, Available: True, File Size: 1.5 MB
Title: Data Science 101, Author: Jane Smith, ISBN: 5544332211, Available: True, File Size: 2.0 MB

Returning '1984'...
Book returned successfully.

Books in the library after returning:
Title: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 1234567890, Available: True
Title: 1984, Author: George Orwell, ISBN: 0987654321, Available: True
Title: Python Programming, Author: John Doe, ISBN: 1122334455, Available: True, File Size: 1.5 MB
Title: Data Science 101, Author: Jane Smith, ISBN: 5544332211, Available: True, File Size: 2.0 MB
```

## Hints or Tips for Completing the Task
- Use the `__init__` method to initialize class attributes.
- Remember to use `self` to refer to instance variables within class methods.
- You can use list comprehensions to filter or manipulate lists of books.
- Test each method individually to ensure they work as expected before integrating them into the main program.

## Additional Resources
- [Python Official Documentation on Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools: Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)

Good luck, and enjoy building your library management system!