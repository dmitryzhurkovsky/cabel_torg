# build application
FROM python:3.10.2-slim-buster

WORKDIR /code

COPY ../Pipfile ../Pipfile.lock /code/

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /code/

RUN chmod +x /code/build/entrypoint.sh

ENTRYPOINT ["sh", "/code/build/entrypoint.sh"]
