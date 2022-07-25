# syntax = docker/dockerfile:1.2
FROM python:3.8


ENV TMWM_WORKDIR /tabdeal/tmwm
ENV PYTHONDONTWRITEBYTECODE 1 # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 # Prevents Python from buffering stdout and stderr

WORKDIR $TMWM_WORKDIR

RUN apt-get update && apt-get install -y vim curl cron build-essential python-dev htop

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt


COPY . .
