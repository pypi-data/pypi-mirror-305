import os
import subprocess
import click
from pathlib import Path

from .utils.helpers.logging import print_info


@click.command()
@click.argument("project_name")
def create_quas_app(project_name):
    """Sets up a new QUAS project with the specified project name."""
    
    print_info(data=f"Setting up project folder")
    
    # Define the repository URL and local paths
    repo_url = "https://github.com/zeddyemy/QUAS.git"
    project_path = Path.cwd() / project_name
    
    # Clone the repository
    subprocess.run(["git", "clone", repo_url, project_name])

    # Replace placeholders in `.env.example` and `config.py`
    env_path = project_path / ".env.example"
    config_path = project_path / "config.py"
    with open(env_path, 'r') as file:
        content = file.read().replace("default-project", project_name)
    with open(env_path, 'w') as file:
        file.write(content)
    
    # Set up virtual environment
    print_info(data=f"Creating Virtual environment")
    os.chdir(project_name)
    subprocess.run(["python", "-m", "venv", ".venv"])
    
    print_info(data=f"Installing dependencies")
    subprocess.run([str(Path(".venv") / "Scripts" / "pip"), "install", "-r", "requirements.txt"])

    print_info(data=f"{project_name} created successfully!")

if __name__ == "__main__":
    create_quas_app()
