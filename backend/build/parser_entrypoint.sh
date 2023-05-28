#!/bin/sh
export PYTHONPATH=$PYTHONPATH:/backend/
echo 'Waiting for migrations are launched.'
sleep 30  # It's used to be sure that all migrations are executed before the parser starts its work.

echo 'Starting parser...'
python src/parser/main.py "/backend"
