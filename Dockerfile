# pull official base image
FROM python:3.8
MAINTAINER MrFlava <thatelitemaili33t@gmail.com>

WORKDIR /newsproject

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /newsproject/
