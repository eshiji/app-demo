FROM python:3.7.9-alpine

WORKDIR /app

COPY requirements.txt .
COPY app/ .
COPY config.py /
COPY run.py /

RUN pip install -r requirements.txt

CMD [ "python", "/run.py" ] 

