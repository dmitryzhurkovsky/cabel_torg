FROM python:3.11.3-slim-buster as base

ENV LANG ru_RU.UTF-8
ENV LC_ALL ru_RU.UTF-8

WORKDIR /backend

RUN apt-get update && apt-get install -y  \
    netcat \
    locales \
    locales-all \
    wkhtmltopdf


COPY ../Pipfile ../Pipfile.lock /backend/
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /backend/

RUN chmod +x /backend/build/backend_entrypoint.sh

FROM base as backend
ENTRYPOINT ["sh", "/backend/build/backend_entrypoint.sh"]

FROM base as parser
ENTRYPOINT ["sh", "/backend/build/parser_entrypoint.sh"]
