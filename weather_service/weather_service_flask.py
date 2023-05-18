from flask import Flask, request, abort, jsonify
import weather_service_func as ws
from prometheus_flask_exporter import PrometheusMetrics
import os 
import redis
import requests
import json


app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/save/", methods=['PUT'])
def save_forecast():
    json_data = request.json
    key = json_data.get("key", None)
    value = json_data.get("value", None)
    if key is None or value is None:
        return jsonify({"error": 'json {"key"=key,"value"=value} must provided'}), 500
    r = redis.Redis(host=os.getenv("REDIS_SERVER"), port=os.getenv("REDIS_PORT"), decode_responses=True)
    if r.set(key, value):
        return jsonify({"set": "OK"})
    return jsonify({"error": 'can`t connect to redis'}), 500

@app.route("/get/")
def get_from_redis():
    key = request.args.get("key", None)
    value = None
    r = redis.Redis(host=os.getenv("REDIS_SERVER"), port=os.getenv("REDIS_PORT"), decode_responses=True)
    value = r.get(key)
    if value is not None:
        return jsonify({"value": value})
    return jsonify({"OK": 'key not found'}), 404

@app.route('/forecast/')
def forecast():
    city, dt = request.args.get("city"), request.args.get("dt")
    if not city or not dt:
        abort(500)
    PORT = os.getenv("PORT")
    req = requests.get(f"http://localhost:{PORT}/get/", params={"key": f"{city}/{dt}"}, timeout=200)
    if req.status_code == 200:
        print("cache found in redis: ", req.status_code, ", ", req.text, flush=True)
        return jsonify({"city": city, "unit": "celsius", "temperature": req.json()["value"], "time": dt})
    weather = ws.getForecastByCity(city, dt)
    re = requests.put(f"http://localhost:{PORT}/save/", json={"key": f"{city}/{dt}", "value": weather["temperature"]}, timeout=200)
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
