# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY cpu_efficiency_test.py /app/cpu_efficiency_test.py

# Install any necessary dependencies
# No additional dependencies are needed for this script

# Specify the command to run the Python script
CMD ["python", "cpu_efficiency_test.py"]
