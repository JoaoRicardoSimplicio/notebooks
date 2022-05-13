FROM python:3.8

ENV PYTHONPATH /app
ENV DJANGO_SETTINGS_MODULE core.settings.base

WORKDIR /app
COPY ./core/requirements/base.txt /app
RUN pip install --upgrade pip
RUN pip install -r base.txt
COPY . /app
