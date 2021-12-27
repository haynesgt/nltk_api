FROM python:3.10-slim-buster

RUN pip3 install pipenv

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY . ./

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --worker-class uvicorn.workers.UvicornWorker nltk-api:app
