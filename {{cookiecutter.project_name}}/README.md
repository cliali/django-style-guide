# {{cookiecutter.project_name}}

## project setup

1- Compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd {{cookiecutter.project_name}}
```

2- Setup Virtualenv with uv
```
pip install uv --user
```
```
uv venv --python 3.13
source .venv/bin/activate
```

3- Install Dependencies
```
uv sync
```

4- Create your env
```
cp .env.example .env
```

5- Spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

6- Create tables
```
python manage.py migrate
```

7- Run the project
```
python manage.py runserver
```