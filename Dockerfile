FROM python:3-alpine

# RUN apt-get update && apt-get -y install gcc
RUN apk update && apk add python3-dev gcc libc-dev libffi-dev

ADD app /app

RUN mkdir /app/cache

RUN pip install -r /app/requirements.txt

CMD [ "python", "/app/main.py" ]

EXPOSE 8080/tcp
