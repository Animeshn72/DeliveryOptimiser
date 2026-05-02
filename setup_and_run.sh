#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Checking for Python 3..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed."
    
    # Detect OS to run the correct installation command
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macOS detected. Downloading and installing Python 3.14.4..."
        curl -O https://www.python.org/ftp/python/3.14.4/python-3.14.4-macos11.pkg
        sudo installer -pkg python-3.14.4-macos11.pkg -target /
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Linux detected. Installing Python 3 via apt..."
        sudo apt update && sudo apt install -y python3 python3-venv
    else
        echo "Unsupported OS for automatic installation. Please install Python manually."
        exit 1
    fi
else
    echo "Python 3 is already installed."
fi

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Execute main.py within the activated environment
echo "Executing the Route Optimizer..."
python src/main.py