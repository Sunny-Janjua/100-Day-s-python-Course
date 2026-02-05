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


# DevOps Starter Project (Complete, Separated Folders)

This folder contains a practical end-to-end DevOps starter implementation with separated code for:

- Python application + tests
- Bash automation scripts
- GitLab CI and Jenkins pipeline definitions
- Docker and Docker Compose
- Kubernetes manifests
- AWS Terraform (ECR/EKS-ready baseline)

## Folder Structure

```text
devops-starter/
├── python-app/
│   ├── app.py
│   ├── health_check.py
│   ├── requirements.txt
│   └── tests/test_app.py
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
```

## Quick Start

1. Run the Python app:
   ```bash
   cd devops-starter/python-app
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```

2. Run tests:
   ```bash
   pytest -q
   ```

3. Build Docker image:
   ```bash
   cd ..
   docker build -f docker/Dockerfile -t devops-starter:local .
   docker run -p 8000:8000 devops-starter:local
   ```

4. Apply Kubernetes manifests:
   ```bash
   cd ../kubernetes
   kubectl apply -f namespace.yaml
   kubectl apply -f configmap.yaml
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   kubectl apply -f hpa.yaml
   ```



