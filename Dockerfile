FROM python:3.8

# Python won’t try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#  Ensures console output looks familiar and is not buffered by Docker
ENV PYTHONUNBUFFERED 1


RUN apt-get update

# Python 3 database connector library compatible with Django
RUN apt-get install -y python3-dev default-libmysqlclient-dev vim

RUN mkdir /src
WORKDIR /src

COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /src

EXPOSE 8000

