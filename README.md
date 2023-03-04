# FastAPI step-by-step guide

This repository allows you to grab the basic concepts behind FastAPI Python library

## 1. Basic virtualenv setup

Make sure you have Python version 3 installed locally on your computer

```
# Create virtual environments base location if needed
mkdir -p ~/.venvs
# Create the virtual environment for this project
python3 -mvenv ~/.venvs/fastapi
# Activate the virtual environment
. ~/.venvs/fastapi/bin/activate
# Import all dependencies
pip install -r requirements.txt
```

The initial **requirements*.txt** files have been produced by running the following commands right after creation of the virtual environment:

```
# Dev part
pip install black # Python code formatter
pip install isort # Python imports statements sorter
pip install autoflake # linter
pip freeze | grep -E '(black|isort|autoflake)==' >> requirements-dev.txt

# Run part
pip install fastapi uvicorn
pip freeze | grep -E '(fastapi|uvicorn)==' >> requirements.txt

# Test part
pip install pytest
pip freeze | grep -E 'pytest==' >> requirements-test.txt
```