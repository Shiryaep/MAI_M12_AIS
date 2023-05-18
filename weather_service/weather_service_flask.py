from flask import Flask, request, abort
import weather_service_func as ws
from prometheus_flask_exporter import PrometheusMetrics
import os


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/forecast/')
def forecast():
    city, dt = request.args.get("city"), request.args.get("dt")
    if not city or not dt:
        abort(500)
    weather = ws.getForecastByCity(city, dt)
    return weather

@app.route('/current/')
def current():
    city = request.args.get("city")
    if not city:
        abort(500)
    weather = ws.getWeatherByCityV2(city)
    return weather


if __name__ == '__main__':
    #print(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=os.getenv("PORT"))
