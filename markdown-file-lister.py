import os
import json

def get_markdown_files(folder_path):
    markdown_files = []

    # Iterate through all items in the specified folder
    for item in os.listdir(folder_path):
        # Create the full path
        full_path = os.path.join(folder_path, item)

        # Check if it's a file and has a .md extension
        if os.path.isfile(full_path) and item.lower().endswith('.md'):
            # Add the relative path to the list
            markdown_files.append(os.path.relpath(full_path, folder_path))

    # Convert the list to JSON
    json_output = json.dumps(markdown_files, indent=2)

    return json_output

# Example usage
#folder_path = './project_docs/'  # Replace with the actual folder path
folder_path = './sample_outputs/ModelBased/python_trainer_output_deepseek_2_5_chat/'
result = get_markdown_files(folder_path)
print(result)
