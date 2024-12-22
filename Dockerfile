# Use multi-arch base image
FROM python:3.11-slim

# Install system dependencies and boto3
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir boto3

# Copy your Python script to the container
COPY HelloWorld.py /app/

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Run your Python script when the container starts
CMD ["python", "HelloWorld.py"]