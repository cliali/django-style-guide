# {{cookiecutter.project_name}}

## project setup

1- Compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project

```bash
cd {{cookiecutter.project_name}}
```

2- Setup Virtualenv with uv

```bash
pip install uv --user
```

```bash
uv venv --python 3.13
source .venv/bin/activate
```

3- Install Dependencies

```bash
uv sync
```

4- Create your env

```bash
cp .env.example .env
```

5- Spin off docker compose

```bash
docker compose -f docker-compose.dev.yml up -d
```

6- Create tables

```bash
python manage.py migrate
```

7- Install tailwindcss with **node**

```bash
npm install
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css
```

8- Run the project

```bash
python manage.py runserver
```
