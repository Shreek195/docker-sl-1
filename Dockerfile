# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY calc.py .

# Command to run the application
CMD ["python", "calc.py"]