# 100-Day-s-python-Course

A practical Python learning repository that now includes both:

- Core Python practice content (scripts + notebook)
- A complete DevOps learning track with ready-to-run starter code

---

## Repository Overview

This repository currently contains:

1. **Python learning artifacts**
   - `day01.py/main.py`
   - `exercise-functions.ipynb`

2. **DevOps theory guide**
   - `DEVOPS_COMPLETE_GUIDE.md`

3. **DevOps implementation starter**
   - `devops-starter/` with separated folders for Python app, Bash scripts, CI/CD, Docker, Kubernetes, and AWS Terraform.

---

## Project Structure

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
```

---

## Python Learning Section

### Run Day 1 Python Script

```bash
python day01.py/main.py
```

### Open Notebook Exercises

Use Jupyter Notebook/Lab:

```bash
jupyter notebook exercise-functions.ipynb
```

---

## DevOps Learning Section

### 1) Read Complete Theory Guide

Start with:

- [`DEVOPS_COMPLETE_GUIDE.md`](DEVOPS_COMPLETE_GUIDE.md)

It follows this sequence:

1. Python for DevOps
2. Bash Scripting
3. GitLab + Jenkins
4. CI/CD Pipelines
5. Docker
6. Kubernetes
7. AWS

### 2) Use Implementation Starter

Go to:

- [`devops-starter/`](devops-starter/)

Then follow:

```bash
cd devops-starter
```

And read:

- [`devops-starter/README.md`](devops-starter/README.md)

for run/build/deploy instructions.

---

## Quick Start (DevOps Starter)

### Run the Python App Locally

```bash
cd devops-starter/python-app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Health endpoint:

- `http://localhost:8000/health`

### Run Health Check Script

```bash
python health_check.py --url http://localhost:8000/health
```

### Run Tests

```bash
pytest -q
```

### Build with Docker

```bash
cd ..
docker build -f docker/Dockerfile -t devops-starter:local .
docker run -p 8000:8000 devops-starter:local
```

### Use Docker Compose

```bash
cd docker
docker compose up --build
```

### Apply Kubernetes Manifests

```bash
cd ../kubernetes
kubectl apply -f namespace.yaml
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

> Create a real secret based on `secret.example.yaml` before production usage.

---

## CI/CD Included

- **GitLab CI:** `devops-starter/ci/gitlab/.gitlab-ci.yml`
- **Jenkins Pipeline:** `devops-starter/ci/jenkins/Jenkinsfile`

Both include test/build pipeline stages and deployment placeholders for your target infrastructure.

---

## AWS IaC Included

Terraform baseline is available under:

- `devops-starter/aws/terraform/`

Current baseline resources include ECR repository and CloudWatch log group, and can be extended to full VPC/EKS architecture.

---

## Recommended Learning Path

1. Run Python files and notebook exercises.
2. Read `DEVOPS_COMPLETE_GUIDE.md` end-to-end.
3. Run `devops-starter/python-app` locally.
4. Run and edit Bash scripts in `devops-starter/scripts`.
5. Build/run Docker image and Compose stack.
6. Apply Kubernetes manifests in a local cluster (kind/minikube).
7. Extend Terraform for your AWS deployment.
8. Connect CI pipeline to your repository and environment.

---

## Notes

- If package installation fails in restricted environments, retry in a network-enabled setup.
- Keep secrets out of git; use secret managers or CI/CD protected variables.
- Prefer small commits with clear messages while extending this repo.

