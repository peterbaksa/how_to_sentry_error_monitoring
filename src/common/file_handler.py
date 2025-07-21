import os

def get_cwd(project_name: str):
    if not project_name in os.getcwd():
        raise FileNotFoundError(f"Project folder name: '{project_name}' not found")
    return os.getcwd().split(project_name)[0]+project_name