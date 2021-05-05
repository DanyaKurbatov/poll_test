FROM python:3.8-alpine

ENV env 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY . /backend/.

RUN adduser -D user
USER user