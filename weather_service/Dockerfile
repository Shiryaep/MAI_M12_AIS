FROM python:3.10.6
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python3", "weather_service_flask.py"]