FROM python:3
USER root

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code


ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . /code/