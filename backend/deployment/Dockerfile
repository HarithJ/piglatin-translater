FROM python:3.7.9-alpine3.12

WORKDIR /home

COPY app.py /home
COPY translater /home/translater

RUN pip install flask
RUN pip install flask_cors
RUN pip install waitress