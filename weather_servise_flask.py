from flask import Flask, request
import urllib.request
import weather_servise as ws


app = Flask(__name__)

@app.route('/forecast/city=<city>&dt=<dt>')
def query_example(city, dt):
    # if key doesn't exist, returns None
    #you can also use lang = request.args['language']
    # if key doesn't exist, second way returns a 400 error
    #language = request.args.get('city')
    #language = 'hey'
    weather = ws.getWeatherByCity(city)

    return '''Weather is {}'''.format(weather)
    #return 'Query String Example'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5015)
