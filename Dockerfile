# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_APP=manage.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URL="postgresql://postgres:postgres@foodorder-db/app"
ENV CELERY_BROKER_URL="amqp://rabbitmq:rabbitmq@rabbitmq:5672"

# RUN apt add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080
COPY . .
CMD ["flask", "run"]
