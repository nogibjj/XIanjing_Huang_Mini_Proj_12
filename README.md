# Xianjing_Huang_Mini_Proj_12
[![Build and Push Docker Image](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_12/actions/workflows/cicd.yml)

## Requirements
* Create a simple python application containerized with a dockerfile.
* Demonstrate running your application within a docker container (using docker run terminal commands).
* Build a docker image in your CI/CD pipeline which will be pushed to Docker Hub or other container management service.

## File Structure
```
├── .github/
│   └── workflows/
│       └── cicd.yml    # Define the GitHub Actions workflow for 
│                       # Checkout repository, Log in to Docker Hub, 
│                       # Build/Push Docker image
├── imgs/
├── .gitignore
├── app.py              # Main Python Flask application
├── Dockerfile          # Instructions for containerizing the app
├── Makefile            # Automation for Docker commands
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Application Functionality
1. Users input their weight (in kilograms) and height (in centimeters).
2. The app calculates the BMI using the formula: BMI = weight / (height in meters)^2.
3. Displays the BMI and the corresponding category (Underweight, Normal, Overweight, or Obesity).
### How It Works:
1. Access the application via a browser at http://127.0.0.1:5001.
2. Enter your weight and height, then submit the form.
3. The app calculates your BMI and displays it with the corresponding category.

<img src="/imgs/003.png" alt="3" style="height:220px;">
<img src="/imgs/004.png" alt="4" style="height:220px;">

## Setup Instructions
### 1. Install Prerequisites
Ensure that Docker is installed on your system.
<img src="/imgs/000.png" alt="0" style="height:40px;">

### 2. Clone the Repository
```sh
git clone https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_12.git
``` 

### 3. Build the Docker Image
Use the make command to build the Docker image:
```sh
make build
```
<img src="/imgs/001.png" alt="1" style="height:80px;">

### 4. Run the Docker Container
Run the Flask application in a Docker container:
```sh
make run
```
The application will be accessible at: http://127.0.0.1:5001.

<img src="/imgs/002.png" alt="2" style="height:120px;">

## Communication between the Host and the Container
1. **Flask App**:
   * Runs inside the container on port 5000 (--port=5000).
   * Listens on all network interfaces (--host=0.0.0.0).
   ```
   CMD ["flask", "run", "--host=0.0.0.0"]
   ```
   is the same as
   ```
   CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
   ```
   since Flask runs on port `5000` by default. 

   If your app needs to run on a different port, you can add `--port=<port>`.
2. **Docker Networking**:
   * Maps host machine's port 5001 to container's port 5000 (-p 5001:5000).
3. **Access the App**:
   * Open http://127.0.0.1:5001 in your browser to interact with the app running inside the container.


## CI/CD Workflow for Deployment to Docker Hub

Set up the following secrets in your GitHub repository under Settings > Secrets and variables > Actions > Repository secrets
* DOCKER_USERNAME: Your Docker Hub username.
* DOCKER_PASSWORD: Your Docker Hub password or access token.

**CI/CD steps**: 
1. Checkout repository
2. Log in to Docker Hub
3. Build Docker image
4. Push Docker image

Here is where you can see the container image pushed to DockerHub:
<img src="/imgs/005.png" alt="5" style="height:180px;">

<img src="/imgs/006.png" alt="6" style="height:220px;">