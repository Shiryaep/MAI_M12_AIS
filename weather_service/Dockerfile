FROM ubuntu:latest
MAINTAINER Pavell ShiryaeP 'shiryaep@gmail.com'
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['weather_service_flask.py']