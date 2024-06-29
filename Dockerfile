# Dockerfile

# Official docker image
FROM python:3.12.1-slim

# Set the working directory in the container
WORKDIR /app

# Set env variables
# Mesa requires that Python is not buffering the output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create a virtual environment in the specified directory
RUN virtualenv venv

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source venv/bin/activate && pip install --no-cache-dir -r requirements.txt"


# Run a default command or shell
CMD ["/bin/bash"]

