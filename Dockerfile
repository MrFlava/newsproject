# pull official base image
FROM python:3.7
MAINTAINER MrFlava <thatelitemaili33t@gmail.com>

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /newsproject

#upgrading pip
RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /newsproject/


