# Use the official Python image as the base image
FROM python:3.11-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN apt update
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port on which the Django app will run
EXPOSE 8000

# Command to run the Django app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]