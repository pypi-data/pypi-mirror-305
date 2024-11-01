import os
import json



def process_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Store file content in a string
            return content
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def create_markdown_file(filepath, content, encoding='utf-8'):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(f"{filepath}.md", "w") as file:
        file.write(content)
    print(f"'{filepath}' has been created with the provided content.")

substrings = {".pytest_cache", "__pycache__", "node_modules"}

def contains_any(substrings, main_string):
    return any(substring in main_string for substring in substrings)



def process_directory(directory)-> dict:
    """Walks through the directory and reads each file's content into a string."""
    file_contents = {}  # Dictionary to store file paths and their contents as strings
    data_store = {}
    
    # Walk through the directory and its subdirectories
    folders_to_ignore = [".pytest_cache", "__pycache__", "node_modules", "documents"]
    avoid = []

        
    
    
    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to exclude specific directories
        dirs[:] = [d for d in dirs if d not in folders_to_ignore]
            
        if root not in avoid:
            for file_name in files:
                file_path = os.path.join(root, file_name)
                content = process_file(file_path)  # Read file into a string
                if content is not None:
                    file_contents[file_path] = content  # Store the string content for each file
                    if file_name:
                        md_content = f"{content}"
                        md_file = file_name.replace(".py", "")
                        create_markdown_file(f"./documents/{md_file}", md_content)
                        data_store[file_path] = {
                            "file_name": file_name,
                            "dir": root,
                            "content": content, 
                        }
    return data_store

