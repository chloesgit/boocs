FROM python:3.9
LABEL maintainer='ewenquim'
EXPOSE 8000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /django-backend

# We changing modules is less frequent than changing code
COPY requirements.txt /django-backend
RUN pip install -r requirements.txt

COPY . /django-backend

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input
