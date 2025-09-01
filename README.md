# 📌 Introduction to DevOps Assignment for Automated Fitness and Gym App.

> ✨ This project aims to log workouts and their durations.

---

## 📖 Table of Contents
- [About](#-about)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Features](#-features)

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

## 🚀 Usage

python src/aceest_fitness.py 

once application is executed, a window pop-ups for entering the workout name and the duration for each workout. 


if the system doesn't support python then docker/pull image can be downloaded. 

podman pull pavanpuvvada66012/my-image:latest

podman run -it --rm my-image:latest


## Features

This project runs automated tests and create a docker image whenever a new commit is being done to the main branch. Also checks for pylint changes whenever a new commit is done to any of the branch in the repository. 



