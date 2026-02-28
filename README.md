# devops-buddy
A simple web application built to help beginner DevOps learners quickly generate Kubernetes commands and Deployment YAML files.

This project demonstrates a complete DevOps workflow:

Build → Containerize → Push → Deploy → Expose
DevOps beginners often struggle with:

Remembering kubectl commands

Writing correct Kubernetes YAML

Understanding basic DevOps tools

As a DevOps learner myself, I built DevOps Buddy to simplify these common tasks.
💡 Solution

DevOps Buddy provides:

✅ Kubernetes Command Generator

✅ Deployment YAML Generator

✅ DevOps Cheat Sheet

It is built using Flask and deployed on a kubeadm Kubernetes cluster.

# Project Structure
```
devops-buddy/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── templates/
    ├── index.html
    ├── command.html
    ├── yaml.html
    └── cheat.html
```

#Local Setup
```bash
git clone https://github.com/ammukaleem/devops-buddy.git
cd devops-buddy

python3 should be pre installed
```bash
pip install -r requirements.txt 
python3 app.py

Access on browser
```bash
http://localhost:5000 or http://your-ip:5000

#Docker Setup
docker pre installed
Run
```bash
docker build -t devops-buddy -t .
docker run -p5000:5000 devops-buddy:letest
Access on browser 
```bash
http://localhost:5000 or http://your-ip:5000

#☸ Kubernetes Deployment (kubeadm Cluster)
step:1
```bash
docker tag devops-buddy <dockerhub-username>/devops-buddy:latest
step:2
```bash
docker push <dockerhub-username>/devops-buddy:latest
step:3
update deployment.yaml
image: <dockerhub-username>/devops-buddy:latest
step:4 
Apply deployment and service files
```bash
kubectl create -f .
step:5 
verify deployment and service
```bash
kubectl get all
# finally Access webpage on http://your-ip:30777












