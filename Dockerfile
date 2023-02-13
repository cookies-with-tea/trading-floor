# pull official base image
FROM python:3.10

# set work directory
WORKDIR /usr/src/trading_floor
ADD . /usr/src/trading_floor

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install poetry
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/trading_floor/docker-entrypoint.sh

ENTRYPOINT ["/usr/src/trading_floor/docker-entrypoint.sh"]