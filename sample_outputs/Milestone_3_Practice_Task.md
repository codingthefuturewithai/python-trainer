# Concept Explanations and Practice Task

# Python Training Plan: Data Structures Milestone

## 1. Concept Explanations

### Lists
- **Definition**: A list is a collection of items in a particular order. Lists are mutable, meaning you can change their content without changing their identity.
- **Example**: `fruits = ['apple', 'banana', 'cherry']`
- **Usage**: Lists are used to store multiple items in a single variable, manage collections of items, and iterate over them in loops. They support operations like appending, removing, and sorting.

### Tuples
- **Definition**: A tuple is similar to a list, but it is immutable. Once a tuple is created, it cannot be modified.
- **Example**: `coordinates = (10, 20)`
- **Usage**: Tuples are used to store collections of items that should not change. They are often used to represent fixed collections of items, like coordinates.

### Dictionaries
- **Definition**: A dictionary is a collection of key-value pairs. Each key is unique, and values can be accessed using their keys.
- **Example**: `student = {'name': 'Alice', 'age': 21}`
- **Usage**: Dictionaries are used to store data values like a map, where you can quickly retrieve the value associated with a specific key. Useful for structured data storage.

### Sets
- **Definition**: A set is an unordered collection of unique items. Sets are mutable, but they do not allow duplicate values.
- **Example**: `unique_numbers = {1, 2, 3}`
- **Usage**: Sets are used to store unique items and perform operations like union, intersection, and difference. They are useful for eliminating duplicate entries.

### Real-world Application
These data structures are fundamental in real-world Python applications for organizing and managing data. Lists and dictionaries are commonly used in data processing, while sets can be used for operations requiring unique elements. Tuples are frequently used for function returns and fixed collections of objects.

## 2. Practice Task

### a. Introduction to the Task
Create a Python script that manages a simple inventory system using the four main data structures: lists, tuples, dictionaries, and sets. This task will help you understand how to implement and manipulate these data structures in a practical context.

### b. Step-by-step Instructions
- **Project Setup**: Create a new directory named `inventory_system`.
- **Main Script File**: Inside the `inventory_system` directory, create a Python script named `inventory.py`.

### c. Detailed Requirements
1. **Inventory Management**:
   - Use a **list** to store items currently in the inventory.
   - Each item should be represented as a **tuple** containing item name and quantity (e.g., `('apple', 10)`).

2. **Operations**:
   - Add new items or update quantities of existing items.
   - Remove items from the inventory.
   - Display all items in the inventory.

3. **Search Functionality**:
   - Use a **dictionary** to map item names to their tuples for quick lookup.
   - Implement a search function that returns the quantity of a specific item.

4. **Unique Categories**:
   - Use a **set** to maintain a collection of unique item categories (e.g., `fruits`, `vegetables`).

### d. Expected Output or Behavior
- The script should allow users to add, remove, and search for items.
- Display a summary of the inventory when requested, showing all items, their quantities, and categories.

### e. Hints or Tips for Completing the Task
- Use functions to encapsulate different operations (e.g., `add_item`, `remove_item`, `search_item`).
- Think carefully about how to update both the list and dictionary when items are added or removed.
- Use set operations to efficiently manage categories.

### f. Additional Resources
- [Python Official Documentation on Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python's Guide to Python Lists](https://realpython.com/python-lists-tuples/)
- [W3Schools Python Dictionary Tutorial](https://www.w3schools.com/python/python_dictionaries.asp)

By completing this task, you will gain practical experience with Python's built-in data structures and understand how they can be used together to solve real-world problems.