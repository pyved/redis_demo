# Dockerfile

# Use the official Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app/

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Install Daphne directly
RUN pip install daphne

# Copy the Django project code into /app
COPY . /app/

# Ensure server_setup.sh is executable
RUN chmod +x /app/server_setup.sh

# Expose the Django and Daphne port
EXPOSE 8000
