# 100-Days-of-Python Course 🐍🚀

A practical Python learning repository that includes:

- Core Python practice (scripts + notebooks)
- A complete DevOps learning track with ready-to-run starter code

This repository is designed for learners who want to **master Python fundamentals** and then **apply them in real-world DevOps workflows**.

---

## 📌 Repository Overview

This repository contains:

### 1. Python Learning Artifacts
- `day01.py/main.py` — Day 1 Python practice script
- `exercise-functions.ipynb` — Hands-on notebook exercises

### 2. DevOps Theory Guide
- `DEVOPS_COMPLETE_GUIDE.md` — End-to-end DevOps concepts

### 3. DevOps Implementation Starter
- `devops-starter/` — Structured starter project including:
  - Python application
  - Bash automation scripts
  - CI/CD pipelines
  - Docker & Docker Compose
  - Kubernetes manifests
  - AWS Infrastructure as Code (Terraform)

---

## 📂 Project Structure

```text
.
├── README.md
├── DEVOPS_COMPLETE_GUIDE.md
├── day01.py/
│   └── main.py
├── exercise-functions.ipynb
└── devops-starter/
    ├── README.md
    ├── .gitignore
    ├── python-app/
    │   ├── app.py
    │   ├── health_check.py
    │   ├── requirements.txt
    │   └── tests/
    │       └── test_app.py
    ├── python-practice/
    │   ├── questions.md
    │   └── solutions.py
    ├── scripts/
    │   ├── backup.sh
    │   ├── cleanup.sh
    │   └── deploy_local.sh
    ├── ci/
    │   ├── gitlab/.gitlab-ci.yml
    │   └── jenkins/Jenkinsfile
    ├── docker/
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   └── .dockerignore
    ├── kubernetes/
    │   ├── namespace.yaml
    │   ├── configmap.yaml
    │   ├── secret.example.yaml
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   ├── ingress.yaml
    │   └── hpa.yaml
    └── aws/terraform/
        ├── providers.tf
        ├── variables.tf
        ├── main.tf
        ├── outputs.tf
        └── README.md
🐍 Python Learning Section
Run Day 1 Python Script
python day01.py/main.py
Open Notebook Exercises
Make sure Jupyter is installed:

jupyter notebook exercise-functions.ipynb
⚙️ DevOps Learning Section
1️⃣ Read the Complete Theory Guide
Start with:

DEVOPS_COMPLETE_GUIDE.md

It follows this learning sequence:

Python for DevOps

Bash Scripting

GitLab & Jenkins

CI/CD Pipelines

Docker

Kubernetes

AWS Basics

2️⃣ Use the DevOps Implementation Starter
Navigate to:

cd devops-starter
Then read:

devops-starter/README.md

for detailed run, build, and deploy instructions.

🚀 Quick Start (DevOps Starter)
Run the Python App Locally
cd devops-starter/python-app
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
Health check endpoint:

http://localhost:8000/health

Run Health Check Script
python health_check.py --url http://localhost:8000/health
Run Tests
pytest -q
Build & Run with Docker
cd ..
docker build -f docker/Dockerfile -t devops-starter:local .
docker run -p 8000:8000 devops-starter:local
Run with Docker Compose
cd docker
docker compose up --build
Apply Kubernetes Manifests
cd ../kubernetes
kubectl apply -f namespace.yaml
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
⚠️ Important:
Create a real secret based on secret.example.yaml before production use.

🔁 CI/CD Included
GitLab CI: devops-starter/ci/gitlab/.gitlab-ci.yml

Jenkins Pipeline: devops-starter/ci/jenkins/Jenkinsfile

Both pipelines include:

Test stage

Build stage

Deployment placeholders (customize for your infrastructure)

☁️ AWS Infrastructure as Code
Terraform configuration is available at:

devops-starter/aws/terraform/

Current baseline includes:

ECR repository

CloudWatch log group

You can extend this to:

VPC

EKS

Load Balancers

IAM roles

🧭 Recommended Learning Path
Run Python scripts and notebook exercises

Read DEVOPS_COMPLETE_GUIDE.md completely

Run the Python app locally

Explore and edit Bash scripts

Build and run Docker images

Deploy to Kubernetes (minikube / kind)

Extend Terraform for AWS

Connect CI/CD pipelines to your repo

📝 Notes & Best Practices
Retry package installation in a network-enabled environment if needed

Never commit secrets to Git

Use CI/CD protected variables or secret managers

Make small, meaningful commits with clear messages

Happy Learning & Building! 🎯


---

If you want next:
- ✅ `devops-starter/README.md` rewritten  
- ✅ Badges (GitHub Actions, Docker, Python)  
- ✅ Professional open-source description  
- ✅ Course-style roadmap (Day 1 → Day 100)

Just tell me 👌
