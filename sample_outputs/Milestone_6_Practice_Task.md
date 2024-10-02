# Practice Task

# Practice Task: Building a Simple Web Application with Flask

## Introduction
In this task, you will apply your Python knowledge to build a simple web application using Flask. This project will help you understand the fundamentals of setting up a Flask application, creating routes and views, and using templates and static files to enhance your web app. By the end of this task, you will have a basic web application that displays a welcome message and an about page.

## Step-by-Step Instructions

### 1. Set Up the Project
- **Create a new project directory**: 
  - Open your terminal or command prompt and create a new directory for your project:
    ```bash
    mkdir flask_web_app
    cd flask_web_app
    ```

- **Create a virtual environment** (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

- **Install Flask**:
  ```bash
  pip install Flask
  ```

- **Create the main Python script file**:
  - Create a file named `app.py` in your project directory.

- **Create additional files**:
  - Create a folder named `templates` for HTML files.
  - Create a folder named `static` for CSS and other static files.

### 2. Detailed Requirements
- **In `app.py`**:
  - Import Flask and create an instance of the Flask class.
  - Define two routes:
    - `/` (home page) that returns a welcome message.
    - `/about` that returns a brief description about the application.
  
- **In the `templates` folder**:
  - Create an HTML file named `home.html` for the home page with a simple welcome message.
  - Create another HTML file named `about.html` for the about page with a description of the application.

- **In the `static` folder**:
  - Create a CSS file named `styles.css` to style your HTML pages (optional).

### 3. Expected Output or Behavior
- When you run the Flask application and navigate to `http://127.0.0.1:5000/`, you should see the welcome message displayed on the home page.
- When you navigate to `http://127.0.0.1:5000/about`, you should see the about page with the application description.
- The pages should be styled according to your CSS file if you choose to include it.

### 4. Hints or Tips for Completing the Task
- Use the `render_template` function from Flask to render your HTML files.
- Make sure to run your Flask application using:
  ```bash
  flask run
  ```
- If you encounter any issues, check the console for error messages that can guide you in debugging.

### 5. Additional Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja2 Template Engine](https://jinja.palletsprojects.com/en/3.0.x/)
- [Flask Routing](https://flask.palletsprojects.com/en/2.0.x/quickstart/#routing)

By completing this task, you will gain hands-on experience with Flask and be better prepared to build more complex web applications in the future. Happy coding!