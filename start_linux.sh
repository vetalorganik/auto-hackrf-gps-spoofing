#!/bin/bash

VENV_DIR=venv
REQUIREMENTS_FILE=requirements.txt

echo "Creating and activating virtual environment..."
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# Check if requirements are already installed
if pip show -r $REQUIREMENTS_FILE > /dev/null; then
    echo "Requirements already installed."
else
    echo "Installing requirements..."
    pip install -r $REQUIREMENTS_FILE
fi

echo "Launching main.py..."
python3 main.py

echo Deactivating virtual environment...
deactivate