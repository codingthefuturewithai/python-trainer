
# User Stories for Generating the First Milestone's Practice Task

**Epic:** Generate and Save First Milestone Practice Task for Python Trainer App

This epic focuses on extending the existing POC by allowing the app to generate a practice task for the first milestone and save it in an appropriately named file. This functionality will further enable users to have a concrete task to start working on after reviewing their training plan.

---

### **User Story 1: Prompt User to Generate First Milestone Practice Task**

- **ID:** `POC-5`
- **Description:**  
  As a **user**, I want the application to ask if I want to generate a practice task for the first milestone of my training plan, so that I can start working on a concrete task related to the milestone.

- **Acceptance Criteria:**  
  - After displaying the generated training plan, the application should prompt the user: “Would you like to generate the practice task for the first milestone? (yes/no)”.
  - If the user selects “yes,” proceed to generate the practice task based on the first milestone’s details.
  - If the user selects “no,” the application should exit gracefully with a message, “You can generate the practice task later by running this command again.”

- **Hints for the Developer:**  
  - Use the `input()` function or `Click` library to capture the user’s response.
  - Store the user’s decision in a variable to conditionally execute the next steps.

---

### **User Story 2: Generate First Milestone Practice Task Using OpenAI GPT**

- **ID:** `POC-6`
- **Description:**  
  As a **developer**, I want the application to generate a practice task for the first milestone using OpenAI GPT, so that the task is tailored to the topics and objectives covered in the milestone.

- **Acceptance Criteria:**  
  - The application should use the first milestone’s objective and topics to create a detailed prompt for OpenAI GPT.
  - The prompt should specify that the response should include a practice task with clear instructions and measurable outputs.
  - The response from OpenAI should be validated to ensure it includes all necessary elements (task description, expected outputs, and any additional hints for the user).

- **Hints for the Developer:**  
  - Create a function like `generate_task_prompt(milestone)` that constructs the prompt using the milestone’s details and interacts with the OpenAI API to get a response.
  - Example prompt structure:  
    ```
    "Create a practice task for the following Python milestone: 
    Objective: {milestone_objective}
    Topics to Cover: {milestone_topics}
    The practice task should include detailed instructions, expected outputs, and hints if necessary."
    ```
  - Store the response from OpenAI as a string and validate it before saving it to a file.

---

### **User Story 3: Save Generated Practice Task to a File**

- **ID:** `POC-7`
- **Description:**  
  As a **user**, I want the generated practice task to be saved in a well-organized file with an appropriate name, so that I can easily identify and access it later.

- **Acceptance Criteria:**  
  - The file name should include the milestone name and a descriptor like `practice_task` (e.g., `Milestone_1_Practice_Task.md`).
  - The content should be saved in Markdown format (`.md`) for readability.
  - The application should confirm the successful save and display the file path to the user.

- **Hints for the Developer:**  
  - Use the `pathlib` library to construct the file name and save path dynamically.
  - Save the practice task as a Markdown file using basic file I/O operations.

  Example file-saving snippet:
  ```python
  task_content = "... Generated task content ..."
  file_name = "Milestone_1_Practice_Task.md"
  save_path = Path("path/to/save/directory") / file_name

  with open(save_path, 'w') as f:
      f.write(task_content)

  print(f"Practice task successfully saved to {save_path}")
  ```

---

These user stories outline the necessary steps to extend the POC with functionality for generating and saving the first milestone's practice task. Let me know if you need additional details or modifications to any of the stories!
