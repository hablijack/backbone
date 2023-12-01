FROM python:3-slim

RUN apt-get update && apt-get -y install gcc

ADD app /app

RUN mkdir /app/cache

RUN pip install -r /app/requirements.txt

CMD [ "python", "/app/main.py" ]

EXPOSE 8080/tcp
