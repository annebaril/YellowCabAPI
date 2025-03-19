FROM python:3.10-slim

WORKDIR /yellowcab_flask

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY static/ yellowcab_flask/static 
COPY templates/ yellowcab_flask/templates 
COPY main_flask.py main_flask.py

CMD ["python", "yellowcab_flask/app.py"]




