# Use the official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir aiogram requests beautifulsoup4

# Expose the port the bot listens on
EXPOSE 8080

# Run the bot when the container launches
CMD ["python", "TampMail-Bot.py"]
