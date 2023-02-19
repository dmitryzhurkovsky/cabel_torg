FROM python:3.10.2-slim-buster

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
