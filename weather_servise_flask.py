from flask import Flask, request
import urllib.request


app = Flask(__name__)

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    #you can also use lang = request.args['language']
    # if key doesn't exist, second way returns a 400 error
    #language = request.args.get('language')
    language = 'hey'

    return '''<h1>The language value is: {}</h1>'''.format(language)
    #return 'Query String Example'

@app.route('/form-example')
def form_example():
    return 'Form Data Example'

@app.route('/json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == '__main__':
    app.run(debug=True, port=5015)
