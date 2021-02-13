FROM python:3.7

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir -r requirements.txt
