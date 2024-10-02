
# User Stories for Generating Practice Tasks for All Milestones and Organizing Files

**Epic:** Generate Practice Tasks for All Remaining Milestones and Organize Saved Files

This epic focuses on adding the ability for the Python Trainer app to generate practice tasks for all remaining milestones based on the generated training plan and save these tasks to files. Additionally, the app will create a dedicated directory to organize all saved files, including the training plan and practice task definitions.

---

### **User Story 1: Create a Dedicated Directory for Organizing Saved Files**

- **ID:** `POC-8`
- **Description:**  
  As a **developer**, I want the app to create a dedicated directory to store the training plan and practice task files, so that all related files are organized in one location.

- **Acceptance Criteria:**  
  - The application should create a directory named `python_trainer_output` in the current working directory.
  - If the directory already exists, the application should not create a duplicate.
  - All subsequent files (training plan and practice task definitions) should be saved in this directory.

- **Hints for the Developer:**  
  - Use the `pathlib` library to create and manage directories.
  - Example code snippet:
    ```python
    from pathlib import Path

    output_dir = Path("python_trainer_output")
    output_dir.mkdir(exist_ok=True)
    print(f"All files will be saved in: {output_dir}")
    ```

---

### **User Story 2: Prompt User to Generate Practice Tasks for All Remaining Milestones**

- **ID:** `POC-9`
- **Description:**  
  As a **user**, I want the application to ask if I want to generate practice tasks for all remaining milestones in the training plan, so that I can have practice tasks ready for each milestone.

- **Acceptance Criteria:**  
  - The application should prompt the user: “Would you like to generate practice tasks for all remaining milestones? (yes/no)”.
  - If the user selects “yes,” the app should proceed to generate practice tasks for all remaining milestones in the training plan.
  - If the user selects “no,” the application should exit gracefully with a message, “You can generate practice tasks for the remaining milestones later by running this command again.”

- **Hints for the Developer:**  
  - Use `input()` or `Click` to capture the user’s response.
  - Store the user’s decision in a variable to conditionally execute the next steps.

---

### **User Story 3: Generate Practice Tasks for All Remaining Milestones**

- **ID:** `POC-10`
- **Description:**  
  As a **developer**, I want the app to iterate through all remaining milestones in the training plan and generate practice tasks for each, so that users have a practice task for every milestone.

- **Acceptance Criteria:**  
  - The application should read the JSON version of the training plan to access all remaining milestones.
  - For each remaining milestone, the application should use OpenAI GPT to generate a practice task based on the milestone’s objectives and topics.
  - The generated practice tasks should be validated to ensure they include all necessary elements (task description, expected outputs, and hints if necessary).

- **Hints for the Developer:**  
  - Use a loop to iterate through the milestones stored in the JSON training plan.
  - Create a function like `generate_practice_task_for_milestone(milestone)` to handle the generation of each practice task.

---

### **User Story 4: Save Practice Tasks to Individual Files**

- **ID:** `POC-11`
- **Description:**  
  As a **user**, I want each generated practice task to be saved to an individual file in the dedicated output directory, so that I can review each task separately.

- **Acceptance Criteria:**  
  - The file name for each practice task should include the milestone number and a descriptor like `practice_task` (e.g., `Milestone_2_Practice_Task.md`).
  - Each file should be saved in the `python_trainer_output` directory.
  - The application should confirm the successful save and display the file path for each generated practice task.

- **Hints for the Developer:**  
  - Use `pathlib` to create and manage file paths dynamically.
  - Save each practice task as a Markdown file using basic file I/O operations.

  Example file-saving snippet:
  ```python
  task_content = "... Generated task content ..."
  file_name = f"Milestone_{milestone_number}_Practice_Task.md"
  save_path = output_dir / file_name

  with open(save_path, 'w') as f:
      f.write(task_content)

  print(f"Practice task successfully saved to {save_path}")
  ```

---

These user stories outline the necessary steps to extend the POC with functionality for generating practice tasks for all milestones and organizing saved files. Let me know if you need additional details or modifications to any of the stories!
