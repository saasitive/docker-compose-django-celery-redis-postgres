# pull official base image
FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app
ADD ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

ADD ./backend /app/backend
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/entrypoint.sh
