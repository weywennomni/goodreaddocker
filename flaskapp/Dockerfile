FROM  alpine:latest
RUN apk add --no-cache python3-dev py3-pip
RUN pip3 install --upgrade pip

FROM mysql:8.0.21

FROM redis:6.0.8
# FROM nginx:1.19.2
FROM python:3.9.0rc1-buster
# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
# FROM gcc:4.9
# FROM alpine:3.4

EXPOSE 5001

COPY . /app

WORKDIR /app

ADD . /app

# RUN pip install --upgrade pip 
# RUN pip install docutils
# RUN apt-get install gcc
# RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi
RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip3 install redis
RUN pip3 install mysql-connector-python

ENTRYPOINT ["python3"]

# CMD ['uwsgi','app.ini']

CMD ["app.py"]
# CMD ["flask", "run", "--host", "0.0.0.0","port","7000"]