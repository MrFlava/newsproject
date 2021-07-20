# pull official base image
FROM python:3.8
MAINTAINER MrFlava <thatelitemaili33t@gmail.com>

WORKDIR /newsproject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /newsproject/
# set environment variables
# ENV PYTHONUNBUFFERED 1


# # set work directory


#
#
# RUN /newsproject/venv/bin/pip install -r requirements.txt

#
# #upgrading pip
# RUN pip install --upgrade pip
#
# COPY ./requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt
#
# COPY . /newsproject/


