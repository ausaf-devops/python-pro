# Use an official Python runtime as the base image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy your Python web server script into the container
COPY webserver.py .

# Expose the port your web server is listening on (port 8000 in this case)
EXPOSE 8000

# Run the Python web server script when the container starts
CMD ["python", "webserver.py"]
