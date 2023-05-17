from flask import Flask, request
import weather_service_func as ws
from prometheus_flask_exporter import PrometheusMetrics
import os


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/forecast/city=<city>&dt=<dt>')
def forecast(city, dt):
    weather = ws.getForecastByCity(city, dt)
    return weather

@app.route('/current/city=<city>')
def current(city):
    weather = ws.getWeatherByCityV2(city)
    return weather
    


if __name__ == '__main__':
    #print(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=os.getenv("PORT"))
