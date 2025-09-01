# 📌 Introduction to DevOps Assignment for Automated Fitness and Gym App.

> ✨ This project aims to log workouts and their durations.

---

## 📖 Table of Contents
- [About](#-about)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)
- [Screenshots](#-screenshots)

---
## 📌 About
Python Project that helps to journal your fitness routines, by logging your Fitness workout and your duration for each workout. 

---
## 🛠 Tech Stack
- 🐍 Python  
- 🐳 Docker 
---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/PavanPuvvada-66012/DevOps_Assignment1.git
# Navigate into the project
cd DevOps_Assignment1

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

```
---
## 🚀 Usage
```
python src/aceest_fitness.py 
```
once application is executed, a window pop-ups for entering the workout name and the duration for each workout. 


if the system doesn't support python then docker/podman pull image can be downloaded. 

```
podman pull pavanpuvvada66012/my-image:latest

podman run --platform=linux/amd64 docker.io/pavanpuvvada66012/my-image:latest  #On Mac as mac is arm64 architecture
```

---
## ⚡ Features

This project runs automated tests and create a docker image whenever a new commit is being done to the main branch. Also checks for pylint changes whenever a new commit is done to any of the branch in the repository. 

---

## 📸 Screenshots

Below Windows pop-ups when program is successfully executed ; Due tk adaptibility issue with mac (text boxes were not showing up , but they do take up data ), below first screenshot is taken from windows env. 

<img width="379" height="261" alt="image" src="https://github.com/user-attachments/assets/51b156ff-9380-4dbd-b25c-d1c7fadcdfb6" />


After adding the workouts

<img width="261" height="179" alt="Screenshot 2025-09-01 at 10 18 49" src="https://github.com/user-attachments/assets/b7d07203-c53d-4181-ae50-0937bd080186" />



When clicked on view workouts

<img width="256" height="211" alt="Screenshot 2025-09-01 at 10 19 02" src="https://github.com/user-attachments/assets/07b03b9d-81be-4fe2-a729-733facd93706" />



If the docker/podman doesn't have display support below warning pops-up and is skipped. 

```
spuvva494@INSML-M0XYJPJ ~ % podman run --platform=linux/amd64 docker.io/pavanpuvvada66012/my-image:latest
⚠️ No display detected. Skipping GUI startup.
```

---


