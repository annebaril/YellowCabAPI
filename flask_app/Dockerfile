FROM python:3.10-slim

WORKDIR /yellowcab_flask

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY static static
COPY templates templates
COPY main_flask.py main_flask.py

CMD ["python", "main_flask.py"]




