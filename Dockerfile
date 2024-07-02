# Ubuntu Docker Image with Python 3.8
FROM ubuntu:20.04

# Set work directory
WORKDIR /code

# Install Python 3 and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install virtualenv
RUN pip3 install --no-cache-dir virtualenv

# Create a virtual environment in the /venv directory
RUN virtualenv /venv

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN /venv/bin/pip3 install --no-cache-dir -r requirements.txt

# Add the virtual environment to PATH & set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/venv/bin:$PATH"

# Copy project files
COPY src /code/src

# Command to run your application
CMD ["python3", "/code/src/gantt_script.py"]
