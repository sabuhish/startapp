Dockerfile='''
FROM  tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app
COPY start.sh /
WORKDIR /app

ENV settings=prod
ENV WEB_CONCURRENCY=1


RUN apt-get update -y &&  pip install --upgrade pip &&  \
    pip install -r requirements.txt && \
    apt-get install -y postgresql-client

'''