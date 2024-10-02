# Practice Task

# Practice Task: Python Fundamentals

## Introduction
In this practice task, you will create a simple program that simulates a basic inventory management system. This task will help you solidify your understanding of Python fundamentals, including data types, control structures, and functions. By the end of this task, you will have a functional program that can add, remove, and display items in an inventory.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a new project**: Open your preferred code editor or IDE and create a new project folder named `inventory_management`.
- **Name the main Python script file**: Inside the `inventory_management` folder, create a new Python file named `inventory.py`.
- **Additional files**: No additional files are needed for this task.

### 2. Detailed Requirements
Your program should meet the following requirements:
1. **Data Structure**: Use a dictionary to represent the inventory, where the keys are item names (strings) and the values are their quantities (integers).
2. **Functions**:
   - `add_item(name: str, quantity: int)`: Adds the specified quantity of the item to the inventory. If the item already exists, increase its quantity.
   - `remove_item(name: str, quantity: int)`: Removes the specified quantity of the item from the inventory. If the quantity exceeds the available amount, display a message indicating insufficient stock.
   - `display_inventory()`: Displays all items in the inventory along with their quantities.
3. **Control Structures**: Implement a simple menu that allows the user to choose between adding an item, removing an item, displaying the inventory, or exiting the program.
4. **User Input**: Use `input()` to get user choices and item details.

### 3. Expected Output or Behavior
When the program runs, it should display a menu like this:
```
1. Add Item
2. Remove Item
3. Display Inventory
4. Exit
```
Based on the user's choice, the program should:
- Prompt for item details if adding or removing an item.
- Display the current inventory when requested.
- Exit the program when the user chooses to do so.

### 4. Hints or Tips for Completing the Task
- Start by defining the main structure of your program, including the inventory dictionary and the functions.
- Use a loop to keep the menu running until the user decides to exit.
- Remember to handle cases where the user might input invalid data (e.g., entering a non-integer for quantity).
- Test each function individually to ensure they work as expected before integrating them into the menu.

### 5. Additional Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [Real Python - Python Dictionaries](https://realpython.com/python-dicts/)
- [Python Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

By completing this task, you will gain practical experience with Python fundamentals that will serve as a strong foundation for your programming journey. Happy coding!