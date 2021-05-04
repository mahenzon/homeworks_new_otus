FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry --help
RUN poetry config virtualenvs.create false

COPY web-app/pyproject.toml web-app/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY web-app .

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000
