FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.7.1

ENV POETRY_VIRTUALENVS_CREATE=false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi
COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH='/app'

RUN python manage.py migrate

RUN mkdir -p media/home/team_members/
RUN mkdir -p media/nuclear_medicine_intro/article/covers
RUN mkdir -p media/nuclear_medicine_intro/article/documents
RUN mkdir -p media/nuclear_medicine_intro/equipment/covers
RUN mkdir -p media/nuclear_medicine_intro/equipment/models