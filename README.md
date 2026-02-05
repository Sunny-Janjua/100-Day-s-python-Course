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

> Note: Create a real secret from `secret.example.yaml` before deploying to production.
