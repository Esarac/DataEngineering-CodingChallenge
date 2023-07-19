# JCompany 🛎️

OLTP API for the insertion and analysis of company employees, departments, and jobs

### Build With ⚙️

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySql](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Azure](https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)

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

2. Run the following command to run the containers 3 containers:

- Flask API (port 5000)
- MySQL (port 3306)
- phpMyAdmin (port 80)

```sh
docker compose up
```

3. Start using the API 🤗.

```sh
http://localhost:5000
```

4. (Optional) You can try the version hosted on Azure 🫡.

```sh
http://52.226.230.142:5000 # API
# or
http://52.226.230.142 # phpMyAdmin
```

### Tests ▶️

If you have the containers up and running, follow the next steps to execute the test cases:

1. Go inside the "jcompany" folder

```sh
cd jcompany
```

2. Create the virtual environment (venv) and install all the dependencies.

```sh
python -m venv venv
# Run "activate" script inside the "venv/Scripts" folder
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the tests

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
