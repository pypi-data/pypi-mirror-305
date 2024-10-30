import os
import shutil

def read_file(file_name):
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path to the directory of this file
    data_path = os.path.join(root_dir, '..', 'data', file_name)
    
    with open(data_path, 'r') as file:
        content = file.read()
    
    return content

def export_file(file_name, destination_dir='.'):
    root_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path to the directory of this file
    data_path = os.path.join(root_dir, '..', 'data', file_name)
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"{file_name} not found in the data directory.")

    # Get the absolute path of the destination directory (defaults to current directory)
    destination_path = os.path.abspath(destination_dir)

    # Copy the file to the destination directory
    shutil.copy(data_path, os.path.join(destination_path, file_name))
    
    return f"File {file_name} exported successfully to {destination_path}."
