FROM python:3.8.13

WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r dev-requirements.txt

