from flask import Flask, request
import weather_service_func as ws


app = Flask(__name__)

@app.route('/forecast/city=<city>&dt=<dt>')
def forecast(city, dt):
    weather = ws.getForecastByCity(city, dt)
    return weather

@app.route('/current/city=<city>')
def current(city):
    weather = ws.getWeatherByCityV2(city)
    return weather
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5015)
