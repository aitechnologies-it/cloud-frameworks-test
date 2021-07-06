FROM python:3.8.9-slim-buster
COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /wd
WORKDIR /wd

CMD ["gunicorn", "-c", "python:gunicorn-config", "app:create_app()"]