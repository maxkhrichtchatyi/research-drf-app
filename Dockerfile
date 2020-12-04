FROM python:3.8-alpine
MAINTAINER Max Khrichtchatyi

ENV PYTHONBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
WORKDIR /app
COPY ./app/ /app

RUN adduser -D app
USER app
