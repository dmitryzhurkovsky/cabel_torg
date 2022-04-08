# Initailization
FROM python:3.10.2-slim-buster as requirements-stage

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# build application
FROM python:3.10.2-slim-buster

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

RUN chmod +x /code/build/entrypoint.sh

ENTRYPOINT ["sh", "/code/build/entrypoint.sh"]
