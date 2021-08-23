FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
RUN mkdir /Docker
ENV STATIC_URL /static
ENV STATIC_PATH /Docker/static
COPY ./requirements.txt /Docker/requirements.txt
RUN pip install -r /Docker/requirements.txt