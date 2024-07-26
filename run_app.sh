#!/bin/bash

# Set the working directory
cd "C:\Users\USER\LA_Project-1"

# Activate virtual environment (if using)
# source /path/to/your/venv/bin/activate

# Check if required file exists
if [ ! -f "matrix_calculator.py" ]; then
  echo "Error: matrix_calculator.py not found!"
  exit 1
fi

# Run the Streamlit app
echo "Starting Streamlit app..."
streamlit run matrix_calculator.py

# Optional: Run in background and log output
# nohup streamlit run matrix_calculator.py > streamlit.log 2>&1 &
