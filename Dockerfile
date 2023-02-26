FROM python:3.10.9

EXPOSE 5000/tcp

ADD . /app

COPY requirements.txt /app/requirements.txt

COPY gunicorn_config.py /app

WORKDIR /app

RUN pip3 --no-cache-dir install -r requirements.txt && \
    chgrp -R 0 /app && \
    chmod -R g=u /app

#USER 1001

CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]