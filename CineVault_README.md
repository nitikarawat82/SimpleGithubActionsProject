# 🎬 CineVault — End-to-End DevOps CI/CD Project

CineVault is a simple movie streaming web application built with **Python Flask**.

The main purpose of this project is to understand how a web application moves
from **local development to a running application on AWS** using DevOps practices.

This project demonstrates how we can:

- Build a web application
- Track the code using Git and GitHub
- Containerize the application using Docker
- Automatically test the application using Pytest
- Build Docker images using GitHub Actions
- Store Docker images in Amazon ECR
- Deploy the application on an AWS EC2 server
- Use AWS Systems Manager (SSM) for remote deployment
- Automatically update the running website whenever new code is pushed

### 🚀 Final Result

A code change can follow this complete automated flow:

```text
Developer
    ↓
Git Push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Amazon ECR
    ↓
AWS Systems Manager
    ↓
AWS EC2
    ↓
Docker Container
    ↓
🌐 Running CineVault Website
```

> **The main goal of CineVault is not to build a complex movie application.
> The goal is to understand the DevOps pipeline behind a running web application
> and automate its deployment from GitHub to AWS.**

---

# 🎯 What This Project Teaches

This project covers the complete practical flow of:

```text
Code
 ↓
Version Control
 ↓
Testing
 ↓
Containerization
 ↓
CI
 ↓
Container Registry
 ↓
Cloud Server
 ↓
Automated Deployment
 ↓
Running Website
```

It gives hands-on practice with:

- Git & GitHub
- Linux
- Docker
- Pytest
- GitHub Actions
- AWS IAM
- Amazon ECR
- Amazon EC2
- AWS Systems Manager
- AWS CLI
- CI/CD

---

# 🛠️ Technologies Used

### Application

- Python
- Flask
- HTML
- CSS
- JavaScript

### DevOps

- Git
- GitHub
- Docker
- Pytest
- GitHub Actions

### AWS

- Amazon EC2
- Amazon ECR
- AWS IAM
- AWS Systems Manager (SSM)
- AWS CLI

---

# 📁 Project Structure

```text
SimpleGithubActionsProject/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── movie.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── data/
│   └── movies.py
│
└── tests/
    └── test_app.py
```

---

# 1️⃣ Build the Flask Application

The first step was to build the CineVault web application using **Python Flask**.

The application contains:

- 🏠 Home page
- 🎬 Movie cards
- ⭐ Ratings
- 🔎 Search functionality
- 🎭 Genres
- 📄 Movie details page
- 📱 Responsive UI

The Flask application runs on port **5000**.

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

### Why `0.0.0.0`?

When the application runs inside Docker, it needs to accept connections from
outside the container.

Using:

```python
host="0.0.0.0"
```

allows Flask to listen on all network interfaces.

### 📌 Get the Source Code

You can **fork my GitHub repository** and use the complete source code to
follow the steps in this project.

👉 **[Fork the CineVault Repository](https://github.com/nitikarawat82/SimpleGithubActionsProject)**

After forking, clone your repository:

```bash
git clone https://github.com/<YOUR-USERNAME>/SimpleGithubActionsProject.git
cd SimpleGithubActionsProject
```

---

# 2️⃣ Install the Application Dependencies

The application dependencies are stored in:

```text
requirements.txt
```

Example:

```text
Flask==3.1.2
```

Install them using:

```bash
pip install -r requirements.txt
```

This installs Flask and the packages required by the application.

---

# 3️⃣ Run the Application Locally

Before introducing Docker or AWS, the application was tested locally.

Run:

```bash
python app.py
```

The application starts on:

```text
http://localhost:5000
```

At this stage:

```text
Python Flask
    ↓
Local Machine
    ↓
localhost:5000
```

This confirms that the application itself is working.

---

# 4️⃣ Initialize Git

Once the application was working, Git was used for version control.

Initialize Git:

```bash
git init
```

Check the repository status:

```bash
git status
```

Add the project files:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Initial CineVault project"
```

Now Git is tracking the project.

---

# 5️⃣ Create the GitHub Repository

A GitHub repository was created for the project.

The local repository was connected to GitHub:

```bash
git remote add origin https://github.com/nitikarawat82/SimpleGithubActionsProject.git
```

Check the remote:

```bash
git remote -v
```

Push the code:

```bash
git push -u origin main
```

Now the source code is available on GitHub.

---

# 6️⃣ Create the Dockerfile

The next step was to containerize the application.

A `Dockerfile` was created in the project root.

```dockerfile
# Use the official lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port used by the Flask application
EXPOSE 5000

# Start the Flask application when the container starts
CMD ["python", "app.py"]
```

### Dockerfile explained

### `FROM`

```dockerfile
FROM python:3.12-slim
```

Uses a lightweight official Python image as the base image.

### `WORKDIR`

```dockerfile
WORKDIR /app
```

Creates `/app` as the working directory inside the container.

### `COPY requirements.txt`

```dockerfile
COPY requirements.txt .
```

Copies the dependency file into the container.

### `RUN`

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs the Python dependencies.

### `COPY . .`

```dockerfile
COPY . .
```

Copies the rest of the project files into the container.

### `EXPOSE`

```dockerfile
EXPOSE 5000
```

Documents that the Flask application uses port 5000.

### `CMD`

```dockerfile
CMD ["python", "app.py"]
```

Starts the Flask application when the container starts.

---

# 7️⃣ Build the Docker Image Locally

The Docker image was first tested locally.

Build the image:

```bash
docker build -t cinevault .
```

Docker reads the Dockerfile and creates an image containing:

```text
Python
 +
Flask
 +
Application Code
 +
Dependencies
```

Check the image:

```bash
docker images
```

---

# 8️⃣ Run the Docker Container Locally

Start the container:

```bash
docker run -d -p 5000:5000 --name cinevault-container cinevault
```

### What does `-p 5000:5000` mean?

```text
Host Port 5000
      ↓
Container Port 5000
```

Check the running container:

```bash
docker ps
```

Open:

```text
http://localhost:5000
```

This confirms that CineVault works inside Docker.

### ⚠️ Important

The Docker image created on the local laptop is only for **local testing**.

It is **not** the image used by the AWS deployment.

The actual CI/CD pipeline builds a fresh Docker image on the
**GitHub Actions runner**, pushes it to ECR, and then EC2 pulls that image.

---

# 9️⃣ Create Automated Tests with Pytest

Before automatically deploying the application, tests were added.

The test file is:

```text
tests/test_app.py
```

The tests check important application routes.

### Test 1 — Home Page

```text
GET /
```

Expected:

```text
HTTP 200
```

### Test 2 — Movie Details

```text
GET /movie/1
```

Expected:

```text
HTTP 200
```

### Test 3 — Invalid Movie

```text
GET /movie/999
```

Expected:

```text
HTTP 404
```

Run the tests:

```bash
pytest
```

Expected result:

```text
3 passed
```

---

# 🔟 Create the GitHub Actions Workflow

GitHub Actions was added to automate the CI process.

The workflow file is created inside:

```text
.github/workflows/
```

For example:

```text
.github/
└── workflows/
    └── ci.yml
```

The workflow performs:

```text
Git Push
    ↓
Checkout Code
    ↓
Setup Python
    ↓
Install Dependencies
    ↓
Run Pytest
    ↓
Build Docker Image
```

Example:

```yaml
name: CineVault CI

on:
  push:
    branches: [main]

  pull_request:
    branches: [main]

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest

      - name: Build Docker image
        run: docker build -t cinevault:latest .
```

### What happens after `git push`?

GitHub Actions automatically starts the workflow.

```text
git push
   ↓
GitHub detects the push
   ↓
GitHub Actions starts
   ↓
Code is checked out
   ↓
Python is installed
   ↓
Dependencies are installed
   ↓
Pytest runs
   ↓
Docker image is built
```

---

# 1️⃣1️⃣ Create an Amazon ECR Repository

The next step was to create a Docker image repository in AWS.

**Amazon ECR = Elastic Container Registry**

ECR is used to store Docker images.

A repository named:

```text
cinevault
```

was created.

The repository URI looks like:

```text
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/cinevault
```

ECR becomes the central location from which EC2 can pull the application image.

---

# 1️⃣2️⃣ Create the GitHub Actions IAM User

GitHub Actions needs permission to communicate with AWS.

A dedicated IAM user was created for GitHub Actions.

The user needs permissions for:

```text
ECR
 +
SSM
```

The GitHub Actions IAM user was given:

```text
AmazonEC2ContainerRegistryFullAccess
```

and an SSM policy allowing:

```text
ssm:SendCommand
ssm:GetCommandInvocation
```

### Why use an IAM user here?

GitHub Actions needs AWS credentials to perform actions such as:

- Push the Docker image to ECR
- Send deployment commands to EC2 through SSM

---

# 1️⃣3️⃣ Add GitHub Secrets

AWS credentials should never be written directly inside the workflow file.

GitHub Secrets were created:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECRIMAGE
```

The ECR image secret contains the complete image address:

```text
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/cinevault:latest
```

The workflow reads the secret using:

```yaml
${{ secrets.ECRIMAGE }}
```

### ⚠️ Security

Never commit AWS access keys or secret keys to GitHub.

---

# 1️⃣4️⃣ Configure GitHub Actions to Push to ECR

After building the Docker image, GitHub Actions logs in to AWS ECR.

The flow becomes:

```text
GitHub Actions
      ↓
Docker Build
      ↓
ECR Login
      ↓
Docker Tag
      ↓
Docker Push
      ↓
Amazon ECR
```

The image is now stored in AWS.

This is important because EC2 can later pull the image directly from ECR.

---

# 1️⃣5️⃣ Launch the AWS EC2 Server

An Ubuntu Server EC2 instance was created to run CineVault.

The EC2 server acts as the application server.

```text
AWS EC2
   ↓
Docker
   ↓
CineVault Container
```

---

# 1️⃣6️⃣ Install Docker on EC2

Connect to the EC2 server and install Docker:

```bash
sudo apt update
```

```bash
sudo apt install -y docker.io
```

Start Docker:

```bash
sudo systemctl enable --now docker
```

Check Docker:

```bash
docker --version
```

Allow the current user to use Docker:

```bash
sudo usermod -aG docker $USER
```

Apply the group change:

```bash
newgrp docker
```

Check:

```bash
docker ps
```

---

# 1️⃣7️⃣ Install AWS CLI on EC2

AWS CLI was installed on the EC2 server.

```bash
sudo apt install -y awscli
```

Check the installation:

```bash
aws --version
```

AWS CLI allows EC2 to communicate with AWS services.

For this project it is used to authenticate Docker with ECR.

---

# 1️⃣8️⃣ Configure the EC2 Security Group

The EC2 Security Group was configured to allow traffic on port **5000**.

Inbound rule:

```text
Type: Custom TCP
Port: 5000
Source: 0.0.0.0/0
```

This allows users on the internet to reach the application through port 5000.

The application is accessed as:

```text
http://EC2-PUBLIC-IP:5000
```

---

# 1️⃣9️⃣ Create an IAM Role for EC2

EC2 also needs permissions to communicate with AWS.

An IAM role was created and attached to the EC2 instance.

Important policies include:

```text
AmazonSSMManagedInstanceCore
AmazonEC2ContainerRegistryReadOnly
```

### Why does EC2 need these permissions?

`AmazonSSMManagedInstanceCore`

Allows Systems Manager to manage the EC2 instance.

`AmazonEC2ContainerRegistryReadOnly`

Allows EC2 to access and pull images from ECR.

---

# 2️⃣0️⃣ Verify EC2 with AWS Systems Manager

AWS Systems Manager (SSM) was used to communicate with the EC2 instance.

The EC2 instance appears as:

```text
Online
```

in Systems Manager.

A test command such as:

```bash
docker ps
```

can be sent through SSM.

This confirms that AWS can remotely execute commands on the EC2 server.

---

# 2️⃣1️⃣ Why Use SSM for Deployment?

Without SSM, we could manually connect to EC2 using SSH and run deployment commands.

Instead, the pipeline does:

```text
GitHub Actions
      ↓
AWS Systems Manager
      ↓
EC2
```

GitHub Actions sends deployment commands to EC2 automatically.

This removes the need to manually open the EC2 terminal for every deployment.

---

# 2️⃣2️⃣ Authenticate Docker with ECR on EC2

Before EC2 can pull the private Docker image, Docker must authenticate with ECR.

The command used is:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 162403021035.dkr.ecr.us-east-1.amazonaws.com
```

### Important Concept

There are two separate things here:

```text
IAM Permission
     ↓
AWS allows EC2 to access ECR
```

and:

```text
docker login
     ↓
Docker authenticates with the ECR registry
```

Both are required for the Docker pull to work.

---

# 2️⃣3️⃣ Pull the Docker Image from ECR

After authentication, EC2 pulls the latest image:

```bash
docker pull $ECR_IMAGE
```

The flow is:

```text
Amazon ECR
    ↓
Docker Pull
    ↓
EC2
```

Now the Docker image is available on the EC2 server.

---

# 2️⃣4️⃣ Remove the Previous Container

Before running the new version, the previous CineVault container is removed:

```bash
docker rm -f cinevault-container || true
```

The `-f` forcefully removes the existing container.

The `|| true` prevents the command from failing if the container does not exist.

---

# 2️⃣5️⃣ Run the New Container on EC2

The new container is started using:

```bash
docker run -d \
  -p 5000:5000 \
  --name cinevault-container \
  $ECR_IMAGE
```

### What does this command do?

`-d`

Runs the container in detached/background mode.

`-p 5000:5000`

Maps:

```text
EC2 Port 5000
      ↓
Container Port 5000
```

`--name cinevault-container`

Gives the container a fixed name.

`$ECR_IMAGE`

Uses the Docker image pulled from ECR.

---

# 2️⃣6️⃣ Verify the Running Container

On EC2:

```bash
docker ps
```

The CineVault container should show:

```text
Up
```

You can also check the application from inside EC2:

```bash
curl http://localhost:5000
```

If HTML is returned, Flask is running correctly inside the container.

---

# 2️⃣7️⃣ Access the Live Website

Once the container is running and port 5000 is allowed in the Security Group:

```text
Internet
    ↓
EC2 Public IP : 5000
    ↓
Docker Container : 5000
    ↓
Flask Application
    ↓
🎬 CineVault
```

Open:

```text
http://EC2-PUBLIC-IP:5000
```

Now CineVault is running on AWS.

---

# 2️⃣8️⃣ Test the Complete CI/CD Pipeline

To prove that the deployment is automated, a small change was made to the website:

```html
<p>🚀 Latest CI/CD Deployment Test</p>
```

Then:

```bash
git add .
```

```bash
git commit -m "Test CI/CD deployment"
```

```bash
git push origin main
```

The complete pipeline automatically runs:

```text
Git Push
   ↓
GitHub Actions
   ↓
Pytest
   ↓
Docker Build
   ↓
Docker Image Push
   ↓
Amazon ECR
   ↓
SSM Deployment Command
   ↓
EC2
   ↓
Docker Pull
   ↓
Remove Old Container
   ↓
Run New Container
   ↓
Updated Website
```

The new content appeared on the running CineVault website.

This confirmed that the end-to-end CI/CD deployment was working.

---

# 🔄 Complete Project Flow

```text
                       👩‍💻 DEVELOPER
                            │
                            │ git push
                            ↓
                       🐙 GITHUB
                            │
                            ↓
                  ⚙️ GITHUB ACTIONS
                            │
                            ↓
                    📥 CHECKOUT CODE
                            │
                            ↓
                    🐍 SETUP PYTHON
                            │
                            ↓
                  📦 INSTALL DEPENDENCIES
                            │
                            ↓
                       🧪 PYTEST
                            │
                     Tests Pass
                            │
                            ↓
                    🐳 DOCKER BUILD
                            │
                            ↓
                       🔐 ECR LOGIN
                            │
                            ↓
                     📦 DOCKER PUSH
                            │
                            ↓
                     ☁️ AMAZON ECR
                            │
                            ↓
                 AWS SYSTEMS MANAGER
                            │
                            ↓
                       ☁️ EC2
                            │
                     Docker Login
                            │
                            ↓
                      Docker Pull
                            │
                            ↓
                 Remove Old Container
                            │
                            ↓
                  Run New Container
                            │
                            ↓
                       🌐 WEBSITE
                            │
                            ↓
                    🎬 CINEVAULT
```

---

# 🔐 IAM Architecture

Two different AWS identities are used.

## GitHub Actions IAM User

GitHub Actions uses its IAM credentials to:

```text
GitHub Actions
      ↓
      AWS
   ↙       ↘
ECR Push   SSM Command
```

Its job is mainly to:

- Push Docker images to ECR
- Send deployment commands to EC2

---

## EC2 IAM Role

The EC2 instance uses its IAM role to:

```text
EC2
 ↓
AWS
 ↙   ↘
ECR   SSM
```

Its job is mainly to:

- Pull Docker images from ECR
- Connect to Systems Manager

This keeps the permissions for CI and the EC2 server separate.

---

# 🧠 Important Concepts Learned

### Docker Image vs Container

```text
Docker Image
     ↓
Template / Package
     ↓
Docker Container
     ↓
Running Application
```

### Local Docker vs AWS Docker

The local Docker image is used only for testing:

```text
Laptop
 ↓
Local Docker Image
 ↓
Local Container
 ↓
localhost:5000
```

The AWS deployment uses a separate image:

```text
GitHub Actions
 ↓
Docker Build
 ↓
Amazon ECR
 ↓
EC2
 ↓
Docker Container
 ↓
Live Website
```

The local Docker image is **not required** for the AWS deployment.

---

# 🧪 Troubleshooting Experience

During deployment, several real-world issues were encountered and resolved.

### ECR Secret Name Mismatch

The workflow initially referenced:

```text
ECR_IMAGE
```

while the GitHub Secret was actually named:

```text
ECRIMAGE
```

Because of this, the ECR image value was empty.

The workflow was corrected to use:

```yaml
${{ secrets.ECRIMAGE }}
```

---

### Docker Authentication with ECR

EC2 had ECR permissions through its IAM role, but Docker was initially unable
to pull the private image.

The error indicated that Docker had no registry credentials.

The solution was to authenticate Docker using:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ECR-REGISTRY>
```

After authentication, EC2 could pull the image successfully.

---

### Container Exit / Removal Investigation

The deployment was also checked when the container disappeared.

Docker logs and system checks were used to investigate the issue.

The deployment flow showed that the old container could be removed after
a failed image pull because the deployment command continued to the
`docker rm -f` step.

This helped demonstrate an important real-world DevOps lesson:

> Deployment failures should be investigated from the complete pipeline,
> not only from the application itself.

---

# 💡 What I Learned

Through this project, I gained hands-on experience with:

- Git and GitHub
- Linux
- Flask
- Docker
- Dockerfiles
- Docker images
- Docker containers
- Port mapping
- Pytest
- GitHub Actions
- CI/CD pipelines
- Amazon ECR
- Amazon EC2
- AWS IAM
- IAM users
- IAM roles
- AWS Systems Manager
- AWS CLI
- Security Groups
- Cloud deployment
- Deployment troubleshooting

---

# 🎯 DevOps Concepts Demonstrated

```text
Version Control
       ↓
Continuous Integration
       ↓
Automated Testing
       ↓
Containerization
       ↓
Container Registry
       ↓
Cloud Infrastructure
       ↓
Automated Deployment
       ↓
Running Application
```

The project demonstrates how application code can move from a developer's
machine to a **running website on AWS through an automated CI/CD pipeline**.

---

# 👩‍💻 Author

**Nitika Rawat**

Hands-on DevOps project focused on learning and implementing:

**Docker • GitHub Actions • AWS ECR • AWS EC2 • IAM • SSM • CI/CD**
