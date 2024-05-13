#!/bin/bash
cd ./src

if [[ -x "$(command -v python)" ]]
then
    python_version="$(python --version)" 
    if [[ $python_version == "Python 3"* ]]
    then
        python3 -m venv .venv
        source .venv/bin/activate
        pip3 install -r ./requirements.txt
        python3 main.py
    else
        echo "Your version of Python is too old. Please update it."
    fi
else
    echo 'Error!
    It looks like Python is not installed! This program requires Python to run!
    To install Python, check out https://www.python.org/downloads/'
    exit 1
fi