
# User Stories for Using a Previous Training Plan or Starting Fresh

**Epic:** Provide Option to Use a Previous Training Plan or Start Fresh

This epic focuses on adding functionality to the Python Trainer app that allows the user to either load a previously saved training plan and related practice tasks or start fresh by generating a new plan and practice tasks. This will enable users to resume their training from a previous session without losing progress or create a new learning plan if desired.

---

### **User Story 1: Prompt User to Load Previous Training Plan or Start Fresh**

- **ID:** `POC-12`
- **Description:**  
  As a **user**, I want the application to ask if I want to load a previously saved training plan and practice tasks, so that I can either continue from where I left off or start fresh with a new plan and tasks.

- **Acceptance Criteria:**  
  - The application should prompt the user: “Would you like to load a previously saved training plan and practice tasks? (yes/no)”.
  - If the user selects “yes,” the application should ask for the file path to the saved training plan.
  - If the user selects “no,” the application should proceed to generate a new training plan and practice tasks.

- **Hints for the Developer:**  
  - Use `input()` or `Click` to capture the user’s response.
  - Store the user’s decision in a variable to conditionally execute the next steps.

---

### **User Story 2: Load a Previously Saved Training Plan**

- **ID:** `POC-13`
- **Description:**  
  As a **developer**, I want the app to load a previously saved training plan from a specified file path, so that the app can use the saved data to restore the user’s progress and regenerate related practice tasks if needed.

- **Acceptance Criteria:**  
  - The application should read the user-provided file path and check if a valid training plan file exists in that location.
  - The application should parse the training plan file and extract information such as milestones, objectives, and topics.
  - The app should validate the file format and display an error message if the file is invalid or not in the expected format.

- **Hints for the Developer:**  
  - Use the `json` module to load and parse a saved JSON training plan.
  - Consider creating a helper function like `load_training_plan(file_path)` to handle file validation and parsing.

---

### **User Story 3: Load Related Practice Tasks for the Training Plan**

- **ID:** `POC-14`
- **Description:**  
  As a **developer**, I want the app to load the practice task files related to the previously loaded training plan, so that the user can review previously generated tasks or regenerate them if needed.

- **Acceptance Criteria:**  
  - The application should look for practice task files that match the loaded training plan’s milestones.
  - If a matching practice task file is found, the app should parse the file and display its content to the user.
  - If a practice task file is missing or corrupted, the app should prompt the user to regenerate that specific practice task.

- **Hints for the Developer:**  
  - Use `pathlib` to check for and validate practice task files in the saved directory.
  - Implement a function like `load_practice_task(milestone_number)` to handle loading of individual practice task files.

---

### **User Story 4: Regenerate Training Plan and Practice Tasks if Starting Fresh**

- **ID:** `POC-15`
- **Description:**  
  As a **user**, I want the application to regenerate the training plan and all practice tasks if I choose to start fresh, so that I can begin a new training session without using any previous data.

- **Acceptance Criteria:**  
  - If the user chooses to start fresh, the application should create a new training plan and practice tasks using the previously defined generation logic.
  - The app should overwrite any existing plan and tasks in the `python_trainer_output` directory with the new files.
  - The app should confirm the successful generation and save of all new files to the user.

- **Hints for the Developer:**  
  - Use existing functions for generating the training plan and practice tasks.
  - Implement a mechanism to clear the contents of `python_trainer_output` if the user chooses to start fresh.

---

These user stories outline the necessary steps to add functionality for loading a previous training plan and practice tasks or starting fresh. Let me know if you need additional details or modifications to any of the stories!
