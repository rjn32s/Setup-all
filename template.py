import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

while True:
    project_name = input("Enter the Project Name: ")

    if project_name !='':
        break

logging.info(f"Creating project by name: {project_name}")

# List of files to be created:

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirments.txt",
    "requirments_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]
