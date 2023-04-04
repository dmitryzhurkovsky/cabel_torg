FROM python:3.10.2-slim-buster

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

RUN chmod +x /backend/build/entrypoint.sh

ENTRYPOINT ["sh", "/backend/build/entrypoint.sh"]
