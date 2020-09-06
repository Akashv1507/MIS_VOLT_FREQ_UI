from src.appConfig import getAppConfigDict
from flask import Flask, request, jsonify, render_template
from src.services.rawFrequencyCreationHandler import RawFrequencyCreationHandler
from src.services.derivedFrequencyCreationHandler import DerivedFrequencyCreationHandler
from src.services.rawVoltageCreationHandler import RawVoltageCreationHandler
from src.services.derivedVoltageCreationHandler import DerivedVoltageCreationHandler
from src.services.derivedVdiCreationHandler import DerivedVdiCreationHandler

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
    # in case of post request, create raw frequency and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        print(reqData)
        obj_rawFrequencyCreator = RawFrequencyCreationHandler(configDict['rawFrequencyCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = obj_rawFrequencyCreator.createRawFrequency(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawFrequency.html.j2')

@app.route('/createDerivedFrequency', methods=['GET', 'POST'])
def createDerivedFrequency():
    # in case of post request, create  derived frequency and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        # print(reqData)
        obj_derivedFrequencyCreator = DerivedFrequencyCreationHandler(configDict['derivedFrequencyCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = obj_derivedFrequencyCreator.createDerivedFrequency(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createDerivedFrequency.html.j2')

@app.route('/createRawVoltage', methods=['GET', 'POST'])
def createRawVoltageForm():
    # in case of post request, create raw voltage and return json response
    if request.method == 'POST':
        # reqData = request.get_json()
        # print(reqData)
        startDate= request.form.get('startDate')
        endDate= request.form.get('endDate')
        obj_rawVoltageCreator = RawVoltageCreationHandler(configDict['rawVoltageCreationServiceUrl'])
        startDate = dt.datetime.strptime(startDate, '%Y-%m-%d')
        endDate = dt.datetime.strptime(endDate, '%Y-%m-%d')
        resp = obj_rawVoltageCreator.createRawVoltage(startDate, endDate)
        print(resp)
        return render_template('rawVoltageResp.html.j2',resp=resp, startDate=startDate.date(), endDate=endDate.date())
        # return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createRawVoltage.html.j2')

# @app.route('/createRawVoltage', methods=['Post'])
# def createRawVoltagePost():

    
@app.route('/createDerivedVoltage', methods=['GET', 'POST'])
def createDerivedVoltage():
    # in case of post request, create derived voltage and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        # print(reqData)
        obj_derivedVoltageCreator = DerivedVoltageCreationHandler(configDict['derivedVoltageCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = obj_derivedVoltageCreator.createDerivedVoltage(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createDerivedVoltage.html.j2')

@app.route('/createDerivedVdi', methods=['GET', 'POST'])
def createDerivedVdi():
    # in case of post request, create derived VDI and return json response
    if request.method == 'POST':
        reqData = request.get_json()
        # print(reqData)
        obj_derivedVdiCreator = DerivedVdiCreationHandler(configDict['derivedVdiCreationServiceUrl'])
        startDate = dt.datetime.strptime(reqData['startDate'], '%Y-%m-%d')
        endDate = dt.datetime.strptime(reqData['endDate'], '%Y-%m-%d')
        resp = obj_derivedVdiCreator.createDerivedVdi(startDate, endDate)
        return jsonify(resp), resp['status']
    # in case of get request just return the html template
    return render_template('createDerivedVdi.html.j2')


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    app.run(debug=True)
