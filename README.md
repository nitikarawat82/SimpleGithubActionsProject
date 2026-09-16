# 🎬 CineVault — DevOps CI/CD Project

CineVault is a simple movie streaming web application built with Python Flask,
but the main purpose of this project is to demonstrate how a web application
can be **containerized, tested, deployed, and continuously updated on AWS
using a complete CI/CD pipeline.**

Instead of manually deploying the application every time a change is made,
this project automates the deployment flow:

**Code Push → Automated Testing → Docker Build → Amazon ECR → AWS EC2 → Live Website**

With every new change pushed to GitHub, GitHub Actions automatically runs
the tests, builds a new Docker image, pushes it to Amazon ECR, and deploys
the latest version to an EC2 server using AWS Systems Manager.

The final result is a **running CineVault website hosted on AWS**, with an
automated deployment pipeline behind it.

---

## 🚀 Architecture

```text
Developer
   ↓
Git / GitHub
   ↓
GitHub Actions
   ↓
Pytest
   ↓
Docker Build
   ↓
Amazon ECR
   ↓
AWS Systems Manager (SSM)
   ↓
AWS EC2
   ↓
Docker Container
   ↓
🌐 Live CineVault
```

---

## 📁 Project Structure

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

The CineVault application was created using Flask.

It includes:
- Home page
- Movie cards
- Movie details
- Search
- Genres
- Ratings
- Responsive UI

The Flask application runs on port **5000**.

```python
app.run(host="0.0.0.0", port=5000, debug=True)
```

`0.0.0.0` allows the application to accept connections from outside the container.

### 📌 Get the Source Code

You can fork my GitHub repository and use the complete CineVault source code
to follow along with the deployment steps.

👉 Fork the CineVault Repository

After forking the repository, you can clone it to your local machine:

```
git clone https://github.com/<YOUR-USERNAME>/SimpleGithubActionsProject.git
cd SimpleGithubActionsProject
```

Now you have the complete application code and can continue with the Docker,
CI/CD and AWS deployment steps.

---

# 2️⃣ Test the Application Locally

Before Docker and AWS deployment, the application was tested locally.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

This confirms that the application works before moving to the DevOps pipeline.

---

# 3️⃣ Git and GitHub

Git was used for version control.

```bash
git init
git add .
git commit -m "Initial CineVault project"
```

The project was then connected to GitHub and pushed to the `main` branch.

```bash
git push -u origin main
```

Now GitHub contains the application source code.

---

# 4️⃣ Dockerize the Application

Docker packages the application and its dependencies into a container.

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### What each instruction does

**FROM** — Uses a lightweight Python base image.

**WORKDIR** — Creates `/app` as the working directory.

**COPY requirements.txt** — Copies the dependency file.

**RUN** — Installs Python dependencies.

**COPY . .** — Copies the project into the container.

**EXPOSE** — Documents that the application uses port 5000.

**CMD** — Starts Flask when the container starts.

---

# 5️⃣ Test Docker Locally

Build the image:

```bash
docker build -t cinevault .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name cinevault-container cinevault
```

Check the container:

```bash
docker ps
```

Open:

```text
http://localhost:5000
```

This verifies that CineVault works inside a Docker container.

> **Important:** The Docker image created on the local laptop is only for local testing. The AWS pipeline builds a fresh image on the GitHub Actions runner.

---

# 6️⃣ Automated Testing with Pytest

Pytest was added to automatically test important application routes.

The tests verify:

- Home page → HTTP 200
- Movie details page → HTTP 200
- Invalid movie → HTTP 404

Run:

```bash
pytest
```

Expected result:

```text
3 passed
```
<img width="1082" height="226" alt="image" src="https://github.com/user-attachments/assets/5b3e43e1-1764-4cac-8ec8-738eb875743c" />

---

# 7️⃣ GitHub Actions CI Pipeline

GitHub Actions automates testing and Docker image building.

The workflow is:

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

Every push to `main` triggers the workflow.

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

---

# 8️⃣ Amazon ECR

**Amazon ECR (Elastic Container Registry)** is used to store the Docker image in AWS.

A repository named:

```text
cinevault
```

was created in ECR.

The image is stored in a format like:

```text
ACCOUNT_ID.dkr.ecr.REGION.amazonaws.com/cinevault:latest
```

ECR acts as the central storage location for the Docker image.

---

# 9️⃣ Push Docker Image to ECR

After the Docker image is built, GitHub Actions logs in to AWS and pushes the image to ECR.

```text
GitHub Actions
      ↓
Docker Build
      ↓
ECR Login
      ↓
Docker Push
      ↓
Amazon ECR
```

GitHub Secrets are used for AWS credentials.

Secrets used:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
ECRIMAGE
```

⚠️ AWS secret keys should never be committed to GitHub.

---

# 🔟 Create and Configure EC2

An **Ubuntu Server EC2** instance was created to run CineVault.

Docker was installed:

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable --now docker
```

AWS CLI was also installed on EC2.

The EC2 security group allows TCP traffic on port **5000** so the application can be accessed.

---

# 1️⃣1️⃣ EC2 IAM Role

An IAM role was attached to the EC2 instance.

Important permissions include:

```text
AmazonSSMManagedInstanceCore
AmazonEC2ContainerRegistryReadOnly
```

These permissions allow EC2 to:

- Connect to AWS Systems Manager
- Access ECR
- Pull the Docker image

---

# 1️⃣2️⃣ AWS Systems Manager (SSM)

AWS Systems Manager is used to execute deployment commands on EC2 remotely.

Instead of manually opening the EC2 terminal for every deployment:

```text
GitHub Actions
      ↓
AWS SSM
      ↓
EC2
      ↓
Run deployment commands
```

This makes the deployment automated.

---

# 1️⃣3️⃣ Authenticate Docker with ECR

EC2 must authenticate Docker with ECR before pulling the image.

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 162403021035.dkr.ecr.us-east-1.amazonaws.com
```

### Important concept

**IAM permission** and **Docker registry authentication** are different things.

IAM allows the EC2 instance to access ECR.

`docker login` authenticates Docker with the ECR registry.

---

# 1️⃣4️⃣ Pull the Latest Image

EC2 pulls the image from ECR:

```bash
docker pull $ECR_IMAGE
```

Flow:

```text
Amazon ECR
    ↓
docker pull
    ↓
EC2 Docker
```

---

# 1️⃣5️⃣ Remove the Previous Container

The old CineVault container is removed:

```bash
docker rm -f cinevault-container || true
```

The `|| true` prevents the command from failing if the container does not already exist.

---

# 1️⃣6️⃣ Run the New Container

The latest image is started on EC2:

```bash
docker run -d   -p 5000:5000   --name cinevault-container   $ECR_IMAGE
```

Port mapping:

```text
EC2 Port 5000
      ↓
Container Port 5000
```

The application is then available through the EC2 public IP.

---

# 🔄 Complete CI/CD Flow

```text
                 👩‍💻 Developer
                      │
                  git push
                      ↓
                 🐙 GitHub
                      │
                      ↓
             ⚙️ GitHub Actions
                      │
                      ↓
                 🧪 Pytest
                      │
                 Tests Pass
                      │
                      ↓
                🐳 Docker Build
                      │
                      ↓
                 🔐 ECR Login
                      │
                      ↓
                📦 Docker Push
                      │
                      ↓
                ☁️ Amazon ECR
                      │
                      ↓
                AWS SSM Command
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
                 🌐 CineVault
```

<img width="1660" height="783" alt="Screenshot 2026-09-16 173955" src="https://github.com/user-attachments/assets/3529ad36-a03a-4ec3-a95c-b3729f6ebbb8" />

---

# 🔐 IAM Permission Flow

There are two important AWS identities.

### GitHub Actions IAM User

Used by GitHub Actions for:

```text
GitHub Actions
      ↓
AWS
 ┌───────────────┐
 │ ECR Push      │
 │ SSM Command   │
 └───────────────┘
```

### EC2 IAM Role

Used by EC2 for:

```text
EC2
 ↓
AWS
 ┌──────────────────────┐
 │ ECR Image Pull       │
 │ SSM Management       │
 └──────────────────────┘
```

This separates CI permissions from server permissions.

---

# 🧪 CI/CD Deployment Test

To verify the pipeline, a small change was made to the website:

```html
<p>🚀 Latest CI/CD Deployment Test</p>
```

Then:

```bash
git add .
git commit -m "Test CI/CD deployment"
git push origin main
```

GitHub Actions automatically performed:

```text
Test
 ↓
Docker Build
 ↓
Push to ECR
 ↓
Deploy through SSM
 ↓
Run new container on EC2
 ↓
Updated website
```

<img width="1852" height="992" alt="image" src="https://github.com/user-attachments/assets/26a49d0a-a34e-45c3-ad2c-cd0b2c8b70d1" />
<br>

<br>

The updated content appeared on the live CineVault website, confirming that the complete CI/CD pipeline was working.

<br>
<br>


<img width="1712" height="842" alt="Screenshot 2026-09-16 183442" src="https://github.com/user-attachments/assets/ad5a3b79-7fd0-401e-bbc5-68ee6c5b55a5" />


---

# 💡 What I Learned

This project helped me practice:

- Git and GitHub
- Flask application deployment
- Docker containerization
- Docker images and containers
- Automated testing with Pytest
- GitHub Actions
- Amazon ECR
- Amazon EC2
- AWS Systems Manager
- AWS IAM
- AWS CLI
- Linux
- Cloud deployment troubleshooting
- End-to-end CI/CD automation

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
```

A code change can move from a developer's Git push to a running application on AWS with minimal manual intervention.

---

## 👩‍💻 Author

**Nitika Rawat**

Hands-on DevOps project focused on learning CI/CD, Docker, GitHub Actions and AWS deployment.
