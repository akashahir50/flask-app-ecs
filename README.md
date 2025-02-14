
# flsk-app-ecs

# Setting Up and Running a Flask App with Docker and MySQL

This document outlines the steps to set up and run a Flask application within a Docker container, connected to a MySQL database container.

## Prerequisites

*   A Linux system.
*   Docker installed.
*   Git installed.
*   A GitHub repository containing your Flask application code, including a `Dockerfile`.

## Installation and Setup

1.  **Update Package Lists:**

    ```bash
    sudo apt-get update
    ```

    Updates the local package list, ensuring you have the latest information about available packages.

2.  **Install Docker:**

    ```bash
    sudo apt-get install docker.io
    ```

    Installs the Docker engine and related tools.

3.  **Check Docker Status:**

    ```bash
    sudo systemctl status docker
    ```

    Verifies that the Docker service is running. If it's not, start it with `sudo systemctl start docker`.

4.  **List Running Containers (initially empty):**

    ```bash
    docker ps
    ```

    Lists currently running Docker containers. This will likely be empty at this point.

5.  **Add User to Docker Group (for non-root access):**

    ```bash
    sudo usermod -aG docker $USER
    newgrp docker  # Or log out and back in
    ```

    Adds the current user to the `docker` group, allowing you to run Docker commands without `sudo` after logging out and back in or running `su - $USER`.

6.  **Log in to Docker Hub (if needed):**

    ```bash
    docker login
    ```

    Logs you into Docker Hub if you need to pull private images or push your own.  Not strictly required here if you're only using public images.

7.  **Pull the MySQL Image:**

    ```bash
    docker pull mysql
    ```

    Downloads the latest version of the MySQL Docker image from Docker Hub.

8.  **List Available Docker Images:**

    ```bash
    docker images
    ```

    Lists all downloaded Docker images.

9.  **Run the MySQL Container (with password - SECURE THIS IN PRODUCTION):**

    ```bash
    docker run -d -e MYSQL_ROOT_PASSWORD=your_strong_password mysql
    ```

    Runs a MySQL container in detached mode (`-d`) with the root password set.  **IMPORTANT:** Replace `your_strong_password` with a strong, unique password.  Storing passwords directly in commands is highly insecure for production. Use environment variables or secrets management for production deployments.

10. **Create Projects Directory and Clone Flask App:**

    ```bash
    mkdir projects
    cd projects
    git clone [your git repo link here]
    ```

    Creates a directory for your project and clones your Flask application's code from GitHub. **Replace `[your git repo link here]` with the actual link to your repository.**

11. **Navigate to Flask App Directory:**

    ```bash
    cd flask-app-ecs  # Replace with the actual directory name
    ```

    Navigates into the directory containing your Flask application's code and the `Dockerfile`.

12. **Build the Flask App Docker Image:**

    ```bash
    docker build -t flask-app-ecs .
    ```

    Builds a Docker image for your Flask app, tagging it as `flask-app-ecs`. The `.` specifies the build context (current directory).

13. **Run the Flask App Container:**

    ```bash
    docker run -d -p 80:80 flask-app-ecs
    ```

    Runs the Flask app container in detached mode (`-d`), mapping port 80 on the host to port 80 in the container.

14. **Check IP and Browser Port Access (Troubleshooting):**

    ```bash
    # Get the container ID (if you don't remember it)
    docker ps

    # Check container logs for errors
    docker logs [container ID]

    # Attach to the running container (for debugging)
    docker attach [container ID]  # Use Ctrl+C to detach

    # Open a bash shell inside the running container (for debugging)
    docker exec -it [container ID] bash
    ```

    These commands help troubleshoot if you're having trouble accessing your application. Check the container logs for errors, and use `docker attach` or `docker exec` to debug inside the container.

15. **Connect to MySQL and Create Database:**

    ```bash
    mysql -u root -p  # Enter the MySQL root password when prompted
    show databases;
    create database devops;
    exit
    exit # Exit the container bash session
    ```

    These commands connect to the MySQL server inside the container, list existing databases, and create a new database named `devops`.
