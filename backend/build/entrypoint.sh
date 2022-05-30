#!/bin/sh

until nc -z -v -w30 db 5432
do
  echo 'Waiting for database connection'
  sleep 5
done

alembic upgrade head
gunicorn src.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --reload
