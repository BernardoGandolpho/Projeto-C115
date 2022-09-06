FROM python:3.8-alpine
WORKDIR /usr/src/chatbot

COPY ./requirements.txt /usr/src/chatbot//requirements.txt

RUN set -eux \
&& apk add --no-cache --virtual .build-deps build-base \
libressl-dev libffi-dev gcc musl-dev python3-dev \
&& pip install --upgrade pip setuptools wheel \
&& pip install -r /usr/src/chatbot/requirements.txt \
&& rm -rf /root/.cache/pip

COPY . /usr/src/chatbot