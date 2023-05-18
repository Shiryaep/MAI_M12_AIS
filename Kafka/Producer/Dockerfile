FROM python:3.10.6
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY producer.py /
CMD [ "python3", "producer.py" ]