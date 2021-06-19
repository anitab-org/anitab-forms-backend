FROM python:3.7

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/


