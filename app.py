from flask import Flask
from flask import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('/ endpoint was reached')
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('/status endpoint was reached')

    return response

@app.route('/metrics')
def metrics():
    app.logger.info('/metrics endpoint was reached')
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', format='%(asctime)s, %(message)s', level=logging.DEBUG)
    app.run(host='0.0.0.0')
