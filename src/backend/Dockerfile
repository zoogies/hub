FROM python:3.12.0a1-bullseye
WORKDIR /src/backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "server.py"]