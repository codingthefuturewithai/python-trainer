# Practice Task

# Practice Task: Milestone 5 - Introduction to Third-Party Libraries

## Introduction
In this practice task, you will familiarize yourself with popular third-party libraries in Python, specifically NumPy and Pandas. You will learn how to install these libraries using `pip`, and you will create a small project that demonstrates basic array manipulation with NumPy and data analysis with Pandas.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a New Project**: Start by creating a new directory for your project. You can name it `third_party_libraries_practice`.
- **Main Python Script File**: Inside the project directory, create a new Python file named `main.py`.
- **Additional Files**: You will also need a CSV file for the Pandas part of the task. Create a file named `data.csv` in the same directory with the following sample data:

```csv
Name,Age,Salary
Alice,30,70000
Bob,25,50000
Charlie,35,80000
David,28,60000
Eve,22,45000
```

### 2. Install Required Libraries
Open your terminal or command prompt and navigate to your project directory. Run the following commands to install NumPy and Pandas:

```bash
pip install numpy pandas
```

### 3. Detailed Requirements for the Task
- **NumPy Task**: 
  - In `main.py`, import NumPy and create a NumPy array with the following values: `[1, 2, 3, 4, 5]`.
  - Calculate and print the mean, median, and standard deviation of the array.

- **Pandas Task**:
  - Import Pandas in `main.py`.
  - Load the `data.csv` file into a Pandas DataFrame.
  - Perform the following operations:
    - Print the first 5 rows of the DataFrame.
    - Calculate and print the average salary.
    - Filter and print the names of employees who earn more than $60,000.

### 4. Expected Output or Behavior
When you run `main.py`, you should see output similar to the following:

```
NumPy Array Statistics:
Mean: 3.0
Median: 3.0
Standard Deviation: 1.4142135623730951

Pandas DataFrame:
      Name  Age  Salary
0    Alice   30   70000
1      Bob   25   50000
2  Charlie   35   80000
3    David   28   60000
4      Eve   22   45000

Average Salary: 61000.0
Employees earning more than $60,000: ['Alice', 'Charlie', 'David']
```

### 5. Hints or Tips for Completing the Task
- Make sure to import the libraries at the beginning of your `main.py` file.
- Use `numpy.mean()`, `numpy.median()`, and `numpy.std()` for calculating statistics in NumPy.
- Use `pandas.read_csv()` to load the CSV file into a DataFrame.
- Use DataFrame methods like `.head()`, `.mean()`, and boolean indexing to filter data in Pandas.

### 6. Additional Resources
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Python Package Index (PyPI)](https://pypi.org/) - for exploring more third-party libraries.

By completing this task, you will gain hands-on experience with installing and using third-party libraries in Python, which is essential for data manipulation and analysis. Happy coding!