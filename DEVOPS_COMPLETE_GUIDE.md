# Complete DevOps Documentation (Step-by-Step)

This guide gives you a practical learning path for DevOps from **Python fundamentals** all the way to **AWS deployment**.

---

## Table of Contents

1. [Learning Roadmap](#1-learning-roadmap)
2. [Phase 1: Python for DevOps](#2-phase-1-python-for-devops)
3. [Phase 2: Bash Scripting](#3-phase-2-bash-scripting)
4. [Phase 3: GitLab and Jenkins](#4-phase-3-gitlab-and-jenkins)
5. [Phase 4: CI/CD Pipelines](#5-phase-4-cicd-pipelines)
6. [Phase 5: Docker](#6-phase-5-docker)
7. [Phase 6: Kubernetes](#7-phase-6-kubernetes)
8. [Phase 7: AWS](#8-phase-7-aws)
9. [Capstone Project: End-to-End DevOps Delivery](#9-capstone-project-end-to-end-devops-delivery)
10. [Operational Best Practices](#10-operational-best-practices)
11. [Interview Preparation Checklist](#11-interview-preparation-checklist)

---

## 1) Learning Roadmap

Follow this order to avoid confusion:

1. **Python** (automation logic)
2. **Bash** (Linux CLI automation)
3. **GitLab + Jenkins** (source control and build orchestration)
4. **CI/CD pipelines** (automated testing/deployment)
5. **Docker** (portable runtime)
6. **Kubernetes** (container orchestration at scale)
7. **AWS** (cloud infrastructure and managed services)

Estimated pace:
- Beginner track: 16–20 weeks
- Intermediate track: 10–14 weeks
- Intensive track: 6–8 weeks

---

## 2) Phase 1: Python for DevOps

### 2.1 Why Python in DevOps

Python helps you:
- Automate repetitive tasks (file handling, API calls, monitoring scripts)
- Build tooling (deployment helpers, config generators, health-check scripts)
- Integrate cloud SDKs (e.g., `boto3` for AWS)

### 2.2 Core Topics to Master

1. **Syntax basics**
   - Variables, data types, operators
   - Conditionals (`if/elif/else`)
   - Loops (`for`, `while`)
2. **Functions and modules**
   - Reusable code design
   - Importing custom modules
3. **File operations**
   - Read/write logs, parse configs (JSON/YAML)
4. **Exception handling**
   - `try/except/finally` for reliable automation
5. **Object-oriented basics**
   - Useful for larger automation projects
6. **Virtual environments**
   - `python -m venv venv`
7. **Package management**
   - `pip install ...`
   - pin dependencies in `requirements.txt`

### 2.3 DevOps-Focused Python Skills

- Parse JSON/YAML files
- Use REST APIs with `requests`
- Build CLIs with `argparse`
- Logging with `logging`
- Write unit tests with `pytest`

### 2.4 Example: Health Check Script

```python
import requests
import sys

URL = "https://example.com/health"

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("Service is healthy")
        sys.exit(0)
    else:
        print(f"Service unhealthy: {response.status_code}")
        sys.exit(1)
except Exception as e:
    print(f"Health check failed: {e}")
    sys.exit(2)
```

### 2.5 Python Milestones

- [ ] Build 3 automation scripts (backup, log parser, API checker)
- [ ] Use `pytest` for at least one script
- [ ] Package one script as a command-line tool

---

## 3) Phase 2: Bash Scripting

### 3.1 Why Bash Matters

Bash is critical for:
- Linux server automation
- Build/deploy pipeline scripts
- Quick operational troubleshooting

### 3.2 Core Bash Fundamentals

1. Shebang and execution
   - `#!/usr/bin/env bash`
   - `chmod +x script.sh`
2. Variables and quoting
   - `name="devops"`
   - Use quotes to avoid word splitting
3. Conditionals and loops
   - `if`, `case`, `for`, `while`
4. Functions and exit codes
   - Return meaningful status (`0` success)
5. Pipes and redirection
   - `|`, `>`, `>>`, `2>`, `2>&1`
6. Text tools
   - `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`

### 3.3 Bash Best Practices

- Always use strict mode:

```bash
set -euo pipefail
IFS=$'\n\t'
```

- Validate input parameters
- Use clear logging messages
- Keep scripts idempotent where possible

### 3.4 Example: Backup Script

```bash
#!/usr/bin/env bash
set -euo pipefail

SRC_DIR="/var/log/myapp"
BACKUP_DIR="/backup/myapp"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
ARCHIVE="$BACKUP_DIR/logs_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

tar -czf "$ARCHIVE" "$SRC_DIR"
echo "Backup created: $ARCHIVE"
```

### 3.5 Bash Milestones

- [ ] Write scripts for service restart, backup, cleanup
- [ ] Add cron scheduling for one script
- [ ] Use shellcheck to validate scripts

---

## 4) Phase 3: GitLab and Jenkins

### 4.1 GitLab Essentials

GitLab provides:
- Source control (Git repository)
- Merge requests and code review
- Built-in CI/CD (`.gitlab-ci.yml`)
- Container registry and package registry

#### GitLab Workflow

1. Create branch: `feature/...`
2. Commit changes in small chunks
3. Push branch
4. Open merge request
5. Run pipeline and complete review
6. Merge into protected branch

#### Branching Strategy

- `main`: production-ready
- `develop`: integration branch
- `feature/*`: new features
- `hotfix/*`: production fixes

### 4.2 Jenkins Essentials

Jenkins is a CI/CD automation server:
- Plugin-based ecosystem
- Supports freestyle and pipeline jobs
- Integrates with Git, Docker, Kubernetes, cloud

#### Jenkins Setup Steps

1. Install Jenkins (package manager or Docker)
2. Secure admin account
3. Install required plugins:
   - Git plugin
   - Pipeline plugin
   - Docker plugin
   - Credentials Binding
4. Add credentials (Git, registry, cloud)
5. Configure agents (static or dynamic)

#### Jenkinsfile Basics

```groovy
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo Building application...'
      }
    }
    stage('Test') {
      steps {
        sh 'echo Running tests...'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo Deploying application...'
      }
    }
  }
}
```

### 4.3 GitLab vs Jenkins (Quick View)

- GitLab CI: simpler when using GitLab end-to-end
- Jenkins: highly flexible for complex enterprise orchestration

---

## 5) Phase 4: CI/CD Pipelines

### 5.1 CI/CD Concepts

- **CI (Continuous Integration):** frequent code integration + automated tests
- **CD (Continuous Delivery/Deployment):** automated release process

### 5.2 Standard Pipeline Stages

1. Source checkout
2. Dependency install
3. Static analysis/linting
4. Unit tests
5. Build artifact/container image
6. Security scanning
7. Deploy to staging
8. Integration/e2e tests
9. Approval gate (optional)
10. Deploy to production

### 5.3 GitLab CI Example

```yaml
stages:
  - lint
  - test
  - build
  - deploy

lint:
  stage: lint
  script:
    - pip install flake8
    - flake8 .

test:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest

build:
  stage: build
  script:
    - docker build -t registry.example.com/myapp:$CI_COMMIT_SHA .
    - docker push registry.example.com/myapp:$CI_COMMIT_SHA

deploy:
  stage: deploy
  script:
    - echo "Deploy to staging"
```

### 5.4 CI/CD Best Practices

- Keep pipelines fast (parallel jobs, caching)
- Shift-left security scans (SAST, dependency scanning)
- Use immutable artifacts
- Separate environments with approval policies
- Store secrets in secure vaults, not in Git

---

## 6) Phase 5: Docker

### 6.1 Docker Fundamentals

Key concepts:
- **Image:** read-only package
- **Container:** running instance of image
- **Dockerfile:** recipe to build image
- **Registry:** image storage (Docker Hub, ECR, GitLab registry)

### 6.2 Basic Docker Commands

- `docker build -t myapp:1.0 .`
- `docker run -d -p 8080:8080 myapp:1.0`
- `docker ps`
- `docker logs <container>`
- `docker exec -it <container> bash`

### 6.3 Production-Ready Dockerfile (Python Example)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "app.py"]
```

### 6.4 Docker Compose Example

```yaml
version: '3.9'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - redis
  redis:
    image: redis:7
```

### 6.5 Docker Best Practices

- Use minimal base images (`slim`, `alpine` when suitable)
- Pin image tags
- Avoid running containers as root
- Use multi-stage builds
- Scan images for vulnerabilities

---

## 7) Phase 6: Kubernetes

### 7.1 Kubernetes Core Architecture

- **Control Plane:** API server, scheduler, controller manager, etcd
- **Worker Nodes:** kubelet, kube-proxy, container runtime

### 7.2 Core Resources

1. **Pod** - smallest deployable unit
2. **Deployment** - manages desired pod replicas/rollouts
3. **Service** - stable networking abstraction
4. **ConfigMap/Secret** - configuration and secret data
5. **Ingress** - external HTTP routing
6. **Namespace** - logical cluster partition

### 7.3 Deployment YAML Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: registry.example.com/myapp:1.0.0
        ports:
        - containerPort: 8000
```

### 7.4 Service YAML Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: ClusterIP
```

### 7.5 Common kubectl Commands

- `kubectl get pods -A`
- `kubectl describe pod <pod-name>`
- `kubectl logs <pod-name>`
- `kubectl apply -f deployment.yaml`
- `kubectl rollout status deployment/myapp`

### 7.6 Kubernetes Best Practices

- Set resource requests/limits
- Use readiness/liveness probes
- Prefer rolling updates
- Enforce RBAC and namespace isolation
- Use GitOps for declarative deployments

---

## 8) Phase 7: AWS

### 8.1 AWS Services You Must Know (DevOps)

- **IAM:** authentication/authorization
- **EC2:** virtual machines
- **S3:** object storage
- **RDS:** managed relational DB
- **VPC:** network isolation
- **ECR:** container registry
- **ECS/EKS:** container orchestration
- **Lambda:** serverless compute
- **CloudWatch:** logs/metrics/alarms
- **CodePipeline/CodeBuild:** native CI/CD tools
- **Route 53:** DNS management

### 8.2 Foundational Setup (Step-by-Step)

1. Create AWS account with MFA
2. Create IAM users/roles (avoid root usage)
3. Configure AWS CLI:
   - `aws configure`
4. Build network:
   - VPC + public/private subnets
   - route tables + internet/NAT gateways
5. Choose compute path:
   - EC2 (simple/manual)
   - ECS/EKS (containerized)
6. Configure storage and database
7. Add observability with CloudWatch
8. Automate infrastructure using Terraform/CloudFormation

### 8.3 Container Deployment on AWS (Typical Path)

1. Build Docker image
2. Push image to ECR
3. Deploy to EKS or ECS
4. Expose service through ALB
5. Configure auto scaling
6. Set alarms and dashboards

### 8.4 AWS Security Best Practices

- Principle of least privilege (IAM)
- Encrypt data at rest and in transit
- Rotate keys/secrets regularly
- Use AWS Secrets Manager/SSM Parameter Store
- Enable CloudTrail for audit logging

### 8.5 AWS Cost Optimization Basics

- Right-size instances
- Use auto scaling
- Use Spot instances for non-critical workloads
- Clean unused EBS volumes and snapshots
- Monitor with Cost Explorer/Budgets

---

## 9) Capstone Project: End-to-End DevOps Delivery

Build this to prove full-stack DevOps skills:

### 9.1 Project Goal

Deploy a Python web app using CI/CD into Kubernetes on AWS.

### 9.2 Project Stack

- App: Python (Flask/FastAPI)
- Repo: GitLab
- CI/CD: GitLab CI or Jenkins
- Container: Docker
- Orchestration: Kubernetes (EKS)
- Cloud: AWS

### 9.3 Milestone Plan

1. Build Python API + tests
2. Dockerize app
3. Create GitLab/Jenkins pipeline
4. Deploy to local k8s (kind/minikube)
5. Deploy to EKS
6. Add monitoring/alerts
7. Add security scans and rollback strategy

### 9.4 Deliverables

- Source code repository
- Pipeline config (`.gitlab-ci.yml` or `Jenkinsfile`)
- Kubernetes manifests/Helm chart
- Architecture diagram
- Runbook (deploy, rollback, troubleshoot)

---

## 10) Operational Best Practices

### 10.1 Reliability

- Health checks everywhere
- Automated rollback on failed deployment
- Blue/Green or Canary strategy for critical apps

### 10.2 Security

- SAST/DAST in pipeline
- Dependency scanning
- Secrets scanning and rotation
- RBAC + network policies in Kubernetes

### 10.3 Observability

- Centralized logs
- Metrics + alerting (error rate, latency, saturation)
- Distributed tracing for microservices

### 10.4 Incident Management

- Define severity levels
- Create on-call rotation
- Maintain incident response playbook
- Do postmortems with clear action items

---

## 11) Interview Preparation Checklist

### Hands-On Questions You Should Be Able to Demonstrate

- [ ] Write a Python script to call an API and handle retries
- [ ] Write a Bash script with safe error handling
- [ ] Build and optimize a Docker image
- [ ] Explain and create a CI/CD pipeline
- [ ] Deploy and debug a Kubernetes application
- [ ] Secure and monitor a workload on AWS

### Scenario Questions

- [ ] Pipeline is slow — how do you optimize it?
- [ ] Deployment failed in production — what rollback method?
- [ ] Kubernetes pods keep restarting — how do you debug?
- [ ] AWS bill spiked — what investigation steps?

---

## Suggested Weekly Execution Plan (12 Weeks)

- **Week 1-2:** Python + automation scripts
- **Week 3:** Bash scripting + cron + Linux tools
- **Week 4-5:** GitLab workflows + Jenkins pipelines
- **Week 6-7:** CI/CD design + quality gates
- **Week 8:** Docker + Docker Compose
- **Week 9-10:** Kubernetes fundamentals + deployments
- **Week 11-12:** AWS deployment + monitoring + capstone

---

## Final Advice

- Learn by building, not just reading.
- Keep every project in Git with clean commit history.
- Document runbooks for deployment and recovery.
- Treat security and observability as first-class requirements.

If you finish this roadmap and complete the capstone, you'll have a strong, real-world DevOps profile.
