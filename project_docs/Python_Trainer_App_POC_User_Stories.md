
# User Stories for Initial POC - Python Trainer App

**Epic:** Initial Proof of Concept (POC) for Python Trainer App

The goal of this POC is to prompt the user to collect their experience level, learning goals, and preferences, generate a personalized Python training plan using OpenAI GPT, and save that plan to a file. This will serve as the foundation for the full application.

---

### **User Story 1: Capture User Information**

- **ID:** `POC-1`
- **Description:**  
  As a **new user**, I want the application to ask me a set of questions about my programming experience, Python knowledge, and learning goals, so that it can gather enough information to create a personalized training plan.

- **Acceptance Criteria:**  
  - The application should prompt the user for their programming experience level (e.g., "No programming experience", "Experienced programmer new to Python").
  - The application should prompt the user for their current Python experience (e.g., "Novice", "Beginner").
  - The application should prompt the user for their learning goals (e.g., "Learning Python for fun", "Learning Python for career advancement").
  - The application should ask the user about their preferred learning style (e.g., "Hands-on projects", "Reading and theory-based learning").
  - All user inputs should be validated to ensure completeness before proceeding.

- **Hints for the Developer:**  
  - Use the `argparse` or `Click` library to handle user inputs in the console.
  - Consider using `Pydantic` to model and validate the collected user information.

---

### **User Story 2: Generate OpenAI GPT Prompt Based on User Information**

- **ID:** `POC-2`
- **Description:**  
  As a **developer**, I want the application to generate a structured and detailed prompt for the OpenAI GPT model using the information gathered from the user, so that the LLM can create a tailored Python training plan.

- **Acceptance Criteria:**  
  - The application should use the user-provided experience level, Python knowledge, and learning goals to formulate an OpenAI GPT prompt.
  - The generated prompt should be formatted clearly and provide all necessary context for the LLM to understand the user’s learning needs.
  - The prompt should specify that the response should include a training plan with clear milestone names, objectives, and topics to cover (as outlined in previous docs).

- **Hints for the Developer:**  
  - Create a function like `generate_prompt(user_info)` that takes the user information as input and returns a well-structured prompt for the LLM.
  - Example prompt structure:  
    ```
    "Create a Python training plan for a user with the following profile: 
    Experience level: {experience_level}, 
    Python knowledge: {python_experience}, 
    Learning goal: {learning_goal}, 
    Preferred learning style: {learning_style}. 
    The plan should include several milestones with milestone names, objectives, and topics to cover."
    ```
  - Consider storing the generated prompt for reference before sending it to OpenAI.

---

### **User Story 3: Request Training Plan from OpenAI GPT**

- **ID:** `POC-3`
- **Description:**  
  As a **developer**, I want the application to communicate with OpenAI GPT using the generated prompt, so that it can retrieve a personalized Python training plan for the user.

- **Acceptance Criteria:**  
  - The application should connect to the OpenAI API using the provided API key.
  - The application should send the generated prompt to the OpenAI GPT model and receive a response with the training plan.
  - If the API call fails or times out, the application should display a user-friendly error message and prompt the user to try again.

- **Hints for the Developer:**  
  - Use the `openai` Python library to make requests to the OpenAI API.  
  - Ensure the API key is securely loaded from the `.env` file using the `python-dotenv` library.

  Example code snippet for setting up the OpenAI client:
  ```python
  import openai
  from dotenv import load_dotenv
  import os

  load_dotenv()
  openai.api_key = os.getenv("OPENAI_API_KEY")
  
  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=generate_prompt(user_info),
      max_tokens=1000
  )
  ```

---

### **User Story 4: Save Training Plan to File**

- **ID:** `POC-4`
- **Description:**  
  As a **user**, I want the application to save the generated Python training plan to a file, so that I can review it later.

- **Acceptance Criteria:**  
  - The training plan should be saved in a human-readable format, such as a text file (`training_plan.txt`) or a JSON file (`training_plan.json`).
  - The application should store the file in a specified directory or prompt the user to provide a directory path for saving the plan.
  - The application should confirm to the user that the file has been successfully saved and provide the file location.

- **Hints for the Developer:**  
  - Use the `json` or `text` module to save the file in the desired format.
  - Use `os` and `pathlib` to handle file paths and directory creation, ensuring compatibility across different operating systems.

  Example file-saving snippet:
  ```python
  import json
  from pathlib import Path

  plan = {"milestone1": {...}, "milestone2": {...}}  # Example structure of the training plan

  save_path = Path("path/to/save/directory/training_plan.json")
  with open(save_path, 'w') as f:
      json.dump(plan, f, indent=4)

  print(f"Training plan successfully saved to {save_path}")
  ```

---

These user stories should provide a clear roadmap to building a simple POC for the Python Trainer App. Let me know if you'd like to include additional details or if you need further guidance on any particular story!
