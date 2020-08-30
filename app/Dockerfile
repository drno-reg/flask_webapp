FROM ubuntu:latest
MAINTAINER Nikolay Baranenko 'drno-reg@mail.ru'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-venv build-essential telnet iputils-ping
RUN apt-get install -y gunicorn

RUN ls -las
COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONPATH=/app \
    FLASK_APP=/app/webapp/ \
    FLASK_CONFIG=/app/flask_run.py \
    FLASK_ENV=development \
    FLASK_DEBUG=1

#CMD ["flask", "run", "-p", "5000", "-h", "0.0.0.0"]

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8118", "wsgi:webapp"]
