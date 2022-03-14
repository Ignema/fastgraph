FROM python:3.10

WORKDIR /app
COPY Pipfile* .

RUN pip install pipenv
RUN pipenv install

COPY src ./src
ENTRYPOINT pipenv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8080

EXPOSE 8080