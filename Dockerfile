FROM python:3.7.1

LABEL Author="Pablo Redigonda"
LABEL E-mail="pabloredigonda@gmail.com"
LABEL version="1.0.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

WORKDIR /app

EXPOSE 5000