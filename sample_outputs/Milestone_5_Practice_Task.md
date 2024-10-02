# Practice Task

# Practice Task: Milestone 5 - Introduction to Third-Party Libraries

## Introduction
In this practice task, you will explore and utilize popular Python libraries: `Requests`, `Pandas`, and `Matplotlib`. You will create a simple project that fetches data from an API, processes it, and visualizes the results. This task will help you understand how to work with third-party libraries effectively.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a new project directory**: Name it `data_visualization_project`.
- **Navigate into the project directory**:
  ```bash
  mkdir data_visualization_project
  cd data_visualization_project
  ```
- **Create the main Python script file**: Name it `main.py`.
- **Create a requirements file**: Name it `requirements.txt`.

### 2. Install Required Libraries
In your terminal, run the following command to install the necessary libraries:
```bash
pip install requests pandas matplotlib
```
Make sure to add the installed libraries to your `requirements.txt` file:
```
requests
pandas
matplotlib
```

## Detailed Requirements for the Task
1. **Fetch Data**:
   - Use the `Requests` library to fetch data from a public API. You can use the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API to get a list of posts.
   - Endpoint: `https://jsonplaceholder.typicode.com/posts`

2. **Process Data**:
   - Use the `Pandas` library to convert the fetched JSON data into a DataFrame.
   - Extract the following columns: `userId`, `id`, `title`, and `body`.

3. **Visualize Data**:
   - Use the `Matplotlib` library to create a bar chart that shows the number of posts per `userId`.
   - The x-axis should represent `userId`, and the y-axis should represent the count of posts.

4. **Output**:
   - Save the bar chart as an image file named `posts_per_user.png`.

## Expected Output or Behavior
- When you run the `main.py` script, it should:
  1. Fetch the data from the API.
  2. Process the data into a DataFrame.
  3. Generate a bar chart showing the number of posts per user.
  4. Save the chart as `posts_per_user.png` in the project directory.

## Hints or Tips for Completing the Task
- Make sure to handle any potential errors when making the HTTP request (e.g., check for a successful response).
- Use `pandas.DataFrame.value_counts()` to easily count the number of posts per `userId`.
- When plotting with Matplotlib, remember to call `plt.show()` if you want to display the chart interactively.

## Additional Resources
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [JSONPlaceholder API Documentation](https://jsonplaceholder.typicode.com/)

By completing this task, you will gain hands-on experience with third-party libraries in Python, enhancing your skills in data manipulation and visualization. Happy coding!