FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-cache
ENV PATH="/app/.venv/bin:$PATH"

# Get the django project into the docker container
ADD . /app
