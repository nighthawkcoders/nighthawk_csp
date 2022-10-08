FROM python:3.9-bullseye

WORKDIR /app
COPY . /app

RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="--workers=3 --bind=0.0.0.0:8080"

EXPOSE 8080

CMD [ "gunicorn", "main:app" ]
