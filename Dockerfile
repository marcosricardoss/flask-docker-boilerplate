FROM python:3.6

# app requirements.txt

WORKDIR /usr/src/flaskapp
ARG BUILD_ENV=prod
ADD config/requirements ./requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/$BUILD_ENV.txt

# bootstrap script

ADD start ./start

# tests setup

ADD setup.cfg ./setup.cfg
