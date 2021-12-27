FROM python:3.10-slim-buster

RUN pip3 install pipenv

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system

COPY . ./

CMD exec uvicorn nltk-api:app --port $PORT
