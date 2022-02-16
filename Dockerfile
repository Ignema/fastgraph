FROM python:3.10

WORKDIR /app
COPY pyproject.toml .


RUN pip install poetry
RUN poetry install

COPY src ./src
ENTRYPOINT poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

EXPOSE 8080