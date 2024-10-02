# Practice Task

# Practice Task: Milestone 1 - Python Fundamentals

## Introduction
In this practice task, you will create a simple Python program that simulates a basic shopping cart system. This task will help you solidify your understanding of core Python concepts such as data types, control structures, and functions. By the end of this task, you will have a functional program that allows users to add items to their cart, view the cart, and calculate the total cost.

## Project Setup Instructions

1. **Create a New Project:**
   - Open your preferred code editor or IDE (e.g., VSCode, PyCharm).
   - Create a new folder for your project named `shopping_cart`.

2. **Name the Main Python Script File:**
   - Inside the `shopping_cart` folder, create a new Python file named `shopping_cart.py`.

3. **Additional Files Needed:**
   - No additional files are required for this task.

## Detailed Requirements

1. **Data Types and Variables:**
   - Create a list to hold the items in the shopping cart.
   - Each item should be represented as a dictionary with the following keys: `name`, `price`, and `quantity`.

2. **Control Structures:**
   - Implement a menu that allows the user to choose from the following options:
     1. Add an item to the cart
     2. View the cart
     3. Calculate the total cost
     4. Exit the program
   - Use `if` statements to handle the user's choice and `while` loops to keep the program running until the user decides to exit.

3. **Functions and Scope:**
   - Create the following functions:
     - `add_item(cart)`: Prompts the user for item details and adds the item to the cart.
     - `view_cart(cart)`: Displays all items in the cart along with their quantities and prices.
     - `calculate_total(cart)`: Calculates and returns the total cost of items in the cart.

## Expected Output or Behavior

- When the program runs, it should display a menu with options.
- Based on the user's input, the program should allow them to add items, view the cart, or calculate the total cost.
- The program should continue to run until the user selects the option to exit.

Example interaction:
```
Welcome to the Shopping Cart!
1. Add an item to the cart
2. View the cart
3. Calculate the total cost
4. Exit
Please choose an option: 1
Enter item name: Apple
Enter item price: 0.5
Enter item quantity: 3
Item added to cart!

1. Add an item to the cart
2. View the cart
3. Calculate the total cost
4. Exit
Please choose an option: 2
Your cart:
- Apple: 3 x $0.5

1. Add an item to the cart
2. View the cart
3. Calculate the total cost
4. Exit
Please choose an option: 3
Total cost: $1.5
```

## Hints or Tips for Completing the Task

- Use a `while True` loop to keep the menu running until the user chooses to exit.
- Make sure to handle user input carefully, especially when converting prices and quantities to the appropriate data types.
- Consider using a `try-except` block to handle potential errors when converting input values.

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python - Python Functions](https://realpython.com/defining-functions-in-python/)

Good luck, and have fun coding your shopping cart program!