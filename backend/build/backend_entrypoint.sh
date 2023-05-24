#!/bin/sh
alembic upgrade head
uvicorn src.app:app --reload --host 0.0.0.0 --port 8000 --log-config log_config.ini
