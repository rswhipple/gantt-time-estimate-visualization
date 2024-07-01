# gantt-time-estimate-visualization
A Python script to visualize a imaginary Task Management App's project timeline/build estimation.

### Build and Run the Docker Virtual Env Container

1. **Build the Docker Image**:
   ```sh
   docker build -t my-python-env .
   ```

2. **Run the Docker Container**:
   ```sh
   docker run -it --rm my-python-env
   ```

Adjust -it for interactive mode if needed, and --rm to automatically remove the container when it exits. This command starts a container from the my-python-app image and runs your application as specified in the CMD directive.