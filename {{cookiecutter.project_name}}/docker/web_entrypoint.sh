#!/bin/sh

echo "--> Waiting for db to be ready"
./wait-for-it.sh db:5432

uv venv --python 3.13
uv sync --frozen
export PATH="/app/.venv/bin:$PATH"

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

# Start server
echo "--> Starting web process"
gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers 2