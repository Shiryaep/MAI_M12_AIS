from flask import Flask, request
import urllib.request


app = Flask(__name__)

@app.route('/forecast/city=<city>&dt=<dt>')
def query_example(city, dt):
    # if key doesn't exist, returns None
    #you can also use lang = request.args['language']
    # if key doesn't exist, second way returns a 400 error
    #language = request.args.get('city')
    #language = 'hey'

    return '''<h1>The language value is: {}</h1>'''.format(city)
    #return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5015)
