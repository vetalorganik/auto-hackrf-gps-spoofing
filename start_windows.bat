@echo off

set VENV_DIR=venv
set REQUIREMENTS_FILE=requirements.txt

echo Creating and activating virtual environment...
python -m venv %VENV_DIR%
call %VENV_DIR%\Scripts\activate

echo Installing requirements...
pip install -r %REQUIREMENTS_FILE%

echo Launching main.py...
python main.py

echo "Deactivating virtual environment..."
deactivate