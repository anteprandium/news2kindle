FROM python:3.8-buster

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install -y pandoc \
    && pip3 install -r requirements.txt

COPY src/ src/
COPY config/ config/

CMD ["python3", "src/news2kindle.py"]
