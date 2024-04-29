#!/bin/bash

# Check if Python 3.8 is installed
if ! command -v python3.8 &>/dev/null; then
    echo "Python 3.8 is not installed. Please install it and try again."
    exit 1
fi

# Run the Python script using Python 3.8
python3.8 play.py
