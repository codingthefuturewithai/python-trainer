# Practice Task

# Practice Task: Data Visualization with Matplotlib

## Introduction
In this practice task, you will learn how to visualize data using Matplotlib, a powerful plotting library in Python. You will create various types of plots, customize them with labels and titles, and learn how to save your visualizations as image files. This task will help you understand the basics of data visualization and how to present data effectively.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a New Project**: Start by creating a new directory for your project. You can name it `matplotlib_visualization`.
- **Main Python Script File**: Inside the `matplotlib_visualization` directory, create a new Python file named `visualization.py`.
- **Additional Files**: You will also need a CSV file containing sample data. Create a file named `data.csv` in the same directory with the following content:

```csv
Year,Sales,Expenses
2018,200,150
2019,300,200
2020,400,250
2021,500,300
2022,600,350
```

### 2. Detailed Requirements
- **Import Matplotlib**: In your `visualization.py` file, import the necessary libraries:
  ```python
  import matplotlib.pyplot as plt
  import pandas as pd
  ```
- **Load the Data**: Use Pandas to read the `data.csv` file into a DataFrame.
- **Create a Line Plot**: Plot the `Sales` data over the `Year` using a line plot.
- **Create a Bar Plot**: Create a bar plot for `Expenses` over the `Year`.
- **Create a Scatter Plot**: Create a scatter plot comparing `Sales` and `Expenses`.
- **Customize the Plots**: Add titles, labels for the axes, and legends to each plot.
- **Save the Figures**: Save each plot as a PNG file in the project directory.

### 3. Expected Output or Behavior
When you run the `visualization.py` script, you should see three plots displayed:
1. A line plot showing Sales over the years.
2. A bar plot showing Expenses over the years.
3. A scatter plot comparing Sales and Expenses.

Additionally, three PNG files named `sales_plot.png`, `expenses_plot.png`, and `scatter_plot.png` should be created in your project directory.

### 4. Hints or Tips for Completing the Task
- Use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to add titles and labels to your plots.
- Use `plt.legend()` to add legends to your plots.
- To save the figures, use `plt.savefig('filename.png')` before calling `plt.show()`.
- Make sure to call `plt.show()` after creating each plot to display them.

### 5. Additional Resources
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html): Official documentation for Matplotlib, which includes tutorials and examples.
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html): Official documentation for Pandas, useful for data manipulation and analysis.
- [Data Visualization with Matplotlib](https://realpython.com/python-matplotlib-guide/): A comprehensive guide on using Matplotlib for data visualization.

By completing this task, you will gain hands-on experience with data visualization in Python, which is an essential skill for data analysis and presentation. Happy coding!