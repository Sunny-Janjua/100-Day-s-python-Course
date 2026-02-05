1	# 100-Day-s-python-Course
     2	
     3	A practical Python learning repository that now includes both:
     4	
     5	- Core Python practice content (scripts + notebook)
     6	- A complete DevOps learning track with ready-to-run starter code
     9	
    10	## Repository Overview
    11	
    12	This repository currently contains:
    13	
    14	1. **Python learning artifacts**
    15	   - `day01.py/main.py`
    16	   - `exercise-functions.ipynb`
    17	
    18	2. **DevOps theory guide**
    19	   - `DEVOPS_COMPLETE_GUIDE.md`
    20	
    21	3. **DevOps implementation starter**
    22	   - `devops-starter/` with separated folders for Python app, Bash scripts, CI/CD, Docker, Kubernetes, and AWS Terraform.

    26	## Project Structure
    30	├── README.md
    31	├── DEVOPS_COMPLETE_GUIDE.md
    32	├── day01.py/
    33	│   └── main.py
    34	├── exercise-functions.ipynb
    35	└── devops-starter/
    36	    ├── README.md
    37	    ├── .gitignore
    38	    ├── python-app/
    39	    │   ├── app.py
    40	    │   ├── health_check.py
    41	    │   ├── requirements.txt
    42	    │   └── tests/
    43	    │       └── test_app.py
    44	    ├── python-practice/
    45	    │   ├── questions.md
    46	    │   └── solutions.py
    47	    ├── scripts/
    48	    │   ├── backup.sh
    49	    │   ├── cleanup.sh
    50	    │   └── deploy_local.sh
    51	    ├── ci/
    52	    │   ├── gitlab/.gitlab-ci.yml
    53	    │   └── jenkins/Jenkinsfile
    54	    ├── docker/
    55	    │   ├── Dockerfile
    56	    │   ├── docker-compose.yml
    57	    │   └── .dockerignore
    58	    ├── kubernetes/
    59	    │   ├── namespace.yaml
    60	    │   ├── configmap.yaml
    61	    │   ├── secret.example.yaml
    62	    │   ├── deployment.yaml
    63	    │   ├── service.yaml
    64	    │   ├── ingress.yaml
    65	    │   └── hpa.yaml
    66	    └── aws/terraform/
    67	        ├── providers.tf
    68	        ├── variables.tf
    69	        ├── main.tf
    70	        ├── outputs.tf
    71	        └── README.md
    75	
    76	## Python Learning Section
    77	
    78	### Run Day 1 Python Script
    79	
    80	```bash
    81	python day01.py/main.py
    82	```
    83	
    84	### Open Notebook Exercises
    85	
    86	Use Jupyter Notebook/Lab:
    87	
    88	```bash
    89	jupyter notebook exercise-functions.ipynb
    90	```
    94	## DevOps Learning Section
    95	
    96	### 1) Read Complete Theory Guide
    97	
    98	Start with:
    99	
   100	- [`DEVOPS_COMPLETE_GUIDE.md`](DEVOPS_COMPLETE_GUIDE.md)
   101	
   102	It follows this sequence:
   103	
   104	1. Python for DevOps
   105	2. Bash Scripting
   106	3. GitLab + Jenkins
   107	4. CI/CD Pipelines
   108	5. Docker
   109	6. Kubernetes
   110	7. AWS
   111	
   112	### 2) Use Implementation Starter
   113	
   114	Go to:
   115	
   116	- [`devops-starter/`](devops-starter/)
   117	
   118	Then follow:
   119	
   120	```bash
   121	cd devops-starter
   122	```
   123	
   124	And read:
   125	
   126	- [`devops-starter/README.md`](devops-starter/README.md)
   127	
   128	for run/build/deploy instructions.
   131	
   132	## Quick Start (DevOps Starter)
   133	
   134	### Run the Python App Locally
   135	
   136	```bash
   137	cd devops-starter/python-app
   138	python -m venv .venv
   139	source .venv/bin/activate
   140	pip install -r requirements.txt
   141	python app.py
   142	```
   143	
   144	Health endpoint:
   145	
   146	- `http://localhost:8000/health`
   147	
   148	### Run Health Check Script
   149	
   150	```bash
   151	python health_check.py --url http://localhost:8000/health
   152	```
   153	
   154	### Run Tests
   155	
   156	```bash
   157	pytest -q
   158	```
   159	
   160	### Build with Docker
   161	
   162	```bash
   163	cd ..
   164	docker build -f docker/Dockerfile -t devops-starter:local .
   165	docker run -p 8000:8000 devops-starter:local
   166	```
   167	
   168	### Use Docker Compose
   169	
   170	```bash
   171	cd docker
   172	docker compose up --build
   173	```
   174	
   175	### Apply Kubernetes Manifests
   176	
   177	```bash
   178	cd ../kubernetes
   179	kubectl apply -f namespace.yaml
   180	kubectl apply -f configmap.yaml
   181	kubectl apply -f deployment.yaml
   182	kubectl apply -f service.yaml
   183	kubectl apply -f hpa.yaml
   184	```
   185	
   186	> Create a real secret based on `secret.example.yaml` before production usage.
   189	
   190	## CI/CD Included
   191	
   192	- **GitLab CI:** `devops-starter/ci/gitlab/.gitlab-ci.yml`
   193	- **Jenkins Pipeline:** `devops-starter/ci/jenkins/Jenkinsfile`
   194	
   195	Both include test/build pipeline stages and deployment placeholders for your target infrastructure.
   196	
   199	## AWS IaC Included
   200	
   201	Terraform baseline is available under:
   202	
   203	- `devops-starter/aws/terraform/`
   204	
   205	Current baseline resources include ECR repository and CloudWatch log group, and can be extended to full VPC/EKS architecture.
   208	
   209	## Recommended Learning Path
   210	
   211	1. Run Python files and notebook exercises.
   212	2. Read `DEVOPS_COMPLETE_GUIDE.md` end-to-end.
   213	3. Run `devops-starter/python-app` locally.
   214	4. Run and edit Bash scripts in `devops-starter/scripts`.
   215	5. Build/run Docker image and Compose stack.
   216	6. Apply Kubernetes manifests in a local cluster (kind/minikube).
   217	7. Extend Terraform for your AWS deployment.
   218	8. Connect CI pipeline to your repository and environment.
   223	
   224	- If package installation fails in restricted environments, retry in a network-enabled setup.
   225	- Keep secrets out of git; use secret managers or CI/CD protected variables.
   226	- Prefer small commits with clear messages while extending this repo.

