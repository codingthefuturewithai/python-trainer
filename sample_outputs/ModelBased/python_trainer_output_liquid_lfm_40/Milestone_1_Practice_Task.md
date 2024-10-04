# Concept Explanations and Practice Task

# Concept Explanations

## 1. Advanced Data Structures
Python provides several built-in data structures such as lists, tuples, sets, and dictionaries. Advanced data structures are more complex and are used to handle large amounts of data more efficiently. These include data structures like heaps, stacks, queues, trees, and graphs. 

In real-world Python programming, these data structures are used in various applications. For example, a graph data structure can be used to represent the relationships between different entities in a social network. A queue data structure can be used to manage tasks in a program.

## 2. Object-Oriented Programming
Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. These objects are instances of classes, which define the properties and behaviors of these objects.

In Python, OOP is used to create complex programs and applications. For example, a game can be created using OOP, where each character or object in the game is an instance of a class.

## 3. Functional Programming
Functional Programming is a programming paradigm where programs are built by applying and composing functions. It avoids changing state and mutable data and treats computation as an evaluation of mathematical functions.

In Python, functional programming can be used to write more concise and readable code. It can also be used to write programs that are easier to test and debug.

## 4. Error Handling
Error handling is a process of anticipating, detecting, and recovering from errors or exceptions that occur during the execution of a program. Python provides various mechanisms for error handling, including try/except blocks and raise statements.

In real-world Python programming, error handling is used to make programs more robust and reliable. For example, if a program encounters an error, it can use error handling to print an error message and continue execution.

## 5. Testing
Testing is a process of running a program or component of a program to evaluate one or more properties of interest. Python provides various tools and libraries for testing, including the unittest module and the pytest library.

In Python, testing is used to ensure that programs work as expected and to catch bugs before they cause problems.

# Practice Task

## a. Introduction
The task is to create a simple application that demonstrates the use of advanced data structures in Python. The application will simulate a library system, where books are stored in a graph data structure.

## b. Project Setup
Create a new Python project and name the main Python script file `library.py`. You will also need an additional file to define the graph data structure.

## c. Requirements
1. Define a `Book` class that represents a book in the library. Each book should have a title, author, and ISBN.
2. Define a `Library` class that represents the library. The library should have a graph data structure to store the books.
3. Implement the following methods in the `Library` class:
   - `add_book(book)`: adds a book to the library.
   - `remove_book(ISBN)`: removes a book from the library.
   - `get_books(author)`: returns a list of books by a particular author.
   - `get_books(title)`: returns a list of books with a particular title.
4. Test your library system with a set of books.

## d. Expected Output
Your code should be able to add and remove books from the library, and return a list of books by a particular author or title.

## e. Hints
- For the graph data structure, you can use the `networkx` library in Python.
- Remember to include tests in your code to ensure it works as expected.

## f. Additional Resources
- `networkx` documentation: [link]
- Python `unittest` module documentation: [link]
- Python `pytest` library documentation: [link]