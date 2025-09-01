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


Running the flask application

```
spuvva494@INSML-M0XYJPJ DevOps_Assignment1 % python -m src.app
```
Application is accessible via http://127.0.0.1:5000/ 

```
spuvva494@INSML-M0XYJPJ DevOps_Assignment1 % podman pull pavanpuvvada66012/my-image:latest
spuvva494@INSML-M0XYJPJ DevOps_Assignment1 % podman run -d --name aceest-container -p 5000:5000 --platform=linux/amd64  pavanpuvvada66012/my-image:latest
bb0bf70ef86db30a8a0dc5185b804d421b4510846add0aaf067b0a0f8213251e
```
App is accessible from http://127.0.0.1:5000/

<img width="571" height="235" alt="image" src="https://github.com/user-attachments/assets/54a8bcd5-3f44-4ef3-b114-27c439c0c05f" />


Steps to run the py tests locally , pytest will be installed as part of the requirements

```
spuvva494@INSML-M0XYJPJ DevOps_Assignment1 % pytest -v
=========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.10.11, pytest-8.4.1, pluggy-1.6.0 -- /Users/spuvva494/.pyenv/versions/3.10.11/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/spuvva494/DevOps_Assignment1
collected 5 items

tests/test_aceest_fitness.py::test_homepage_loads PASSED                                                                                                            [ 20%]
tests/test_aceest_fitness.py::test_add_valid_workout PASSED                                                                                                         [ 40%]
tests/test_aceest_fitness.py::test_add_invalid_workout PASSED                                                                                                       [ 60%]
tests/test_aceest_fitness.py::test_view_workouts_empty PASSED                                                                                                       [ 80%]
tests/test_aceest_fitness.py::test_view_workouts_with_data PASSED                                                                                                   [100%]

============================================================================ 5 passed in 0.17s ============================================================================
spuvva494@INSML-M0XYJPJ DevOps_Assignment1 %
```

---


