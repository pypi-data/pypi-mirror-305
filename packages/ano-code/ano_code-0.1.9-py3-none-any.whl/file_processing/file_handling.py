import os
from yaspin import yaspin



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


@yaspin(text="Scanning project...")
def process_directory(directory)-> dict:
    loader = yaspin()
    loader.start()
    """Walks through the directory and reads each file's content into a string."""
    file_contents = {}  # Dictionary to store file paths and their contents as strings
    data_store = {}
    
    # Walk through the directory and its subdirectories
    folders_to_ignore = [".pytest_cache", "__pycache__", "node_modules", "documents", "dist", "ano_code.egg-info", "auto-code-env"]
    avoid = []

    fl = {".py", ".js", ".go", ".ts", ".tsx", ".jsx", ".dart"}
    
    
    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to exclude specific directories
        dirs[:] = [d for d in dirs if d not in folders_to_ignore]
        for filename in files:
        # Check if the file has an excluded extension
            if filename.endswith(tuple(fl)):
                        file_path = os.path.join(root, filename)
                        content = process_file(file_path)  # Read file into a string
                        if content is not None:
                            file_contents[file_path] = content  # Store the string content for each file
                            if filename:
                                md_content = f"{content}"
                                create_markdown_file(f"./documents/{filename}", md_content)
                                data_store[file_path] = {
                                    "file_name": filename,
                                    "dir": root,
                                    "content": content, 
                                }
    loader.stop()
    return data_store

