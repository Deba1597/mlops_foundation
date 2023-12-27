import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# project_name = 'mlops'

list_of_files = [
    f".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/component/__init__.py",
    f"src/component/data_ingestion.py",
    f"src/component/data_transformation.py",
    f"src/component/model_trainer.py",
    f"src/component/model_evaluation.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/training_pipeline.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/utils/__init__.py", 
    f"src/utils/utils.py",
    "src/logger/__init__.py",
    "src/logger/logging.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    'experiment/experiment.ipynb'
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file : {filepath}")
        

    else:
        logging.info(f"{filename} is already exists")