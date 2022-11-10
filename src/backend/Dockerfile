# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /src/backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "server.py"]