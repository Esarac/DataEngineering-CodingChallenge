# JCompany 🛎️

OLTP API for the insertion and analysis of company employees, departments, and jobs

### Build With ⚙️

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySql](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

## Getting Started ✅

### Prerequisites ⬅️

- Install *Python*
- Install *Docker Desktop*
- Clone repository

### Installation 🔃

1. Open the terminal and go inside the project folder.

```sh
cd /../../project_folder
```

2. Run the following command to run the database and *phpMyAdmin* (running on port 8888)

```sh
docker compose up
```

3. Go inside the "jcompany" folder, create the virtual environment (venv) and install all the dependencies.

```sh
cd jcompany
python -m venv venv
# Run "activate" script inside the "venv/Scripts" folder
pip install -r requirements.txt
```

4. Run the application (port 5000).

```sh
py manage.py run
```

### Tests ▶️

In order to run the test cases, go inside the "jcompany" folder and execute the following command:

```sh
py manage.py test
```

## Endpoints 📡

### Departments 🏢

| URL | Method | Input | Output |
|---|---|---|---|
| .../departments | GET | - | List of departments
| .../departments | POST | List of departments | - |
| .../departments/csv | POST | csv of departments | - |

### Jobs 🔨

| URL | Method | Input | Output |
|---|---|---|---|
| .../jobs | GET | - | List of jobs
| .../jobs | POST | List of jobs | - |
| .../jobs/csv | POST | csv of jobs | - |

### Employees 👷‍♂️

| URL | Method | Input | Output |
|---|---|---|---|
| .../employees | GET | - | List of employees
| .../employees | POST | List of employees | - |
| .../employees/csv | POST | csv of employees | - |

### Stats 📊

| URL | Method | Input | Output |
|---|---|---|---|
| .../stats/a | GET | - | Number of employees hired in 2021 for each job and department, divided by quarter |
| .../stats/b | GET | - | Department that hired more employees than the mean of employees hired in 2021 |
