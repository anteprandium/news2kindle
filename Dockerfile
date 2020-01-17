FROM python:3.8.0-alpine3.10

COPY src/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src/ src/
COPY config/ config/

CMD ["python3", "src/news2kindle.py"]
