#!/bin/bash
PORT=${PORT-8080}
gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 --worker-class uvicorn.workers.UvicornWorker --reload nltk_api:app 
