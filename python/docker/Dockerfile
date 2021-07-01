FROM python:3.8.9-alpine
COPY src/requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /wd
WORKDIR /wd

# RUN addgroup --gid 1001 --system  pythonminimal && adduser -u 1001 --group pythonminimal --disabled-password --system && chown -R pythonminimal:pythonminimal /wd
# USER pythonminimal
CMD ["gunicorn", "-c", "python:gunicorn-config", "app:create_app()"]