# Practice Task

# Practice Task: Object-Oriented Programming in Python

## Introduction
In this practice task, you will implement a simple library management system using Object-Oriented Programming (OOP) principles in Python. This task will help you understand how to create classes and objects, utilize inheritance and polymorphism, and apply encapsulation and abstraction in your code.

## Project Setup Instructions

1. **Create a New Project**: 
   - Create a new directory for your project called `library_management_system`.

2. **Name the Main Python Script File**: 
   - Inside the `library_management_system` directory, create a file named `main.py`.

3. **Additional Files Needed**: 
   - You will also create a file named `library.py` to define your classes.

## Detailed Requirements for the Task

1. **Define Classes**:
   - Create a class named `Book` with the following attributes:
     - `title` (string)
     - `author` (string)
     - `isbn` (string)
     - `available` (boolean, default to `True`)
   - Include methods to:
     - Borrow a book (set `available` to `False`)
     - Return a book (set `available` to `True`)
     - Display book information.

2. **Create a Library Class**:
   - Create a class named `Library` that contains:
     - A list to store `Book` objects.
     - Methods to:
       - Add a book to the library.
       - Remove a book from the library.
       - Search for a book by title or author.
       - List all available books.

3. **Implement Inheritance**:
   - Create a subclass named `EBook` that inherits from `Book` and adds an additional attribute:
     - `file_size` (float, in MB)
   - Override the method to display book information to include the file size.

4. **Encapsulation**:
   - Ensure that the attributes of the `Book` and `Library` classes are private and provide public methods to access and modify them.

5. **Polymorphism**:
   - Implement a method in both `Book` and `EBook` classes that returns a string representation of the object, demonstrating polymorphism.

## Expected Output or Behavior

- When you run `main.py`, it should:
  - Create instances of `Book` and `EBook`.
  - Add them to the `Library`.
  - Demonstrate borrowing and returning books.
  - List all available books.
  - Search for a specific book by title or author.
  - Display the information of each book, including the file size for eBooks.

## Hints or Tips for Completing the Task

- Start by defining the `Book` class and its methods before moving on to the `Library` class.
- Use Python's built-in list methods to manage the collection of books in the library.
- Remember to use the `__str__` method to provide a string representation of your objects.
- Test each method as you implement it to ensure it works correctly before moving on to the next.

## Additional Resources

- [Python Official Documentation on Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools: Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)

Good luck with your library management system! Happy coding!