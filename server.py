from src.appConfig import getAppConfigDict
from flask import Flask, request, jsonify, render_template
from src.services.rawFrequencyCreationHandler import RawFrequencyCreationHandler

import datetime as dt
# from waitress import serve

app = Flask(__name__)

# get application config
configDict = getAppConfigDict()

# Set the secret key to some random bytes
# app.secret_key = appConfig['flaskSecret']

@app.route('/')
def hello():
    return render_template('home.html.j2')


@app.route('/createRawFrequency', methods=['GET', 'POST'])
def createRawFrequency():
    # in case of post request, create raw outages and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        obj_frequencyCreator = RawFrequencyCreationHandler(configDict['rawFrequencyCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = obj_frequencyCreator.createRawFrequency(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawFrequency.html.j2')

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    app.run(debug=True)
