Markdown
# 100-Days-of-Python Course 🐍🚀

Welcome to the **100-Days-of-Python** repository! This is a comprehensive, practical journey designed to help you master Python fundamentals and seamlessly transition into real-world **DevOps workflows**.

## 📌 Repository Overview

This repository is divided into three core pillars:

1.  **Python Mastery**: Daily scripts and interactive notebooks to build a rock-solid foundation.
2.  **DevOps Theory**: A complete guide covering the "Why" and "How" of modern infrastructure.
3.  **DevOps Implementation**: A production-ready starter project featuring CI/CD, Containerization, and Infrastructure as Code (IaC).

---

## 🛠️ Tech Stack

* **Language:** Python 3.x, Bash
* **Containerization:** Docker, Docker Compose
* **Orchestration:** Kubernetes (K8s)
* **CI/CD:** GitLab CI, Jenkins
* **Cloud & IaC:** AWS, Terraform
* **Testing:** Pytest

---

## 📂 Project Structure

```text
.
├── README.md                   # Main documentation
├── DEVOPS_COMPLETE_GUIDE.md    # End-to-end DevOps concepts
├── day01.py/                   # Daily Python practice
│   └── main.py
├── exercise-functions.ipynb    # Hands-on Jupyter notebooks
└── devops-starter/             # Integrated DevOps Project
    ├── python-app/             # Core Flask/FastAPI application & tests
    ├── python-practice/        # DevOps-specific Python logic
    ├── scripts/                # Bash automation (Backup, Deploy, Cleanup)
    ├── ci/                     # Pipeline definitions (GitLab/Jenkins)
    ├── docker/                 # Containerization configs
    ├── kubernetes/             # K8s Manifests (Deployment, Service, HPA)
    └── aws/terraform/          # Infrastructure as Code for AWS
🚀 Quick Start (DevOps Starter)
Follow these steps to get the sample application and infrastructure up and running.

1. Run the Python App Locally
Bash
cd devops-starter/python-app
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
2. Run Automated Tests
Bash
pytest tests/test_app.py -v
3. Containerize with Docker
Bash
# Build the image
docker build -f docker/Dockerfile -t devops-starter:local .

# Run the container
docker run -d -p 8000:8000 devops-starter:local
4. Deploy to Kubernetes
Bash
cd devops-starter/kubernetes
kubectl apply -f namespace.yaml
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
📈 Learning Path
Days 1-30: Python Basics (Syntax, Loops, Functions, Data Structures).

Days 31-60: Advanced Python & Scripting (OS module, Requests, Automation).

Days 61-100: The DevOps Shift (Docker, K8s, CI/CD Pipelines, and Terraform).

🤝 Contributing
Contributions are welcome! If you have a script or a DevOps best practice to add, feel free to open a Pull Request.

Founder: Hussnain Mulazam (Sunny Janjua)


---

### What I improved:
* **Visual Hierarchy**: Used better headers and horizontal rules to separate the "Python" part from the "DevOps" part.
* **Tech Stack Section**: Added a quick-glance list of tools, which is great for your portfolio.
* **Clearer Instructions**: Added comments to the bash commands (like the Windows activate command) to make it more user-friendly.
* **Roadmap**: Included a brief timeline to explain the "100 Days" concept.

Would you like me to help you write the content for the `DEVOPS_COMPLETE_GUIDE.md` file next?
