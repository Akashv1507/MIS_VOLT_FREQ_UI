import requests
import datetime as dt
from src.typeDefs.rawVoltageCreationResp import RawVoltageCreationResp


class RawVoltageCreationHandler():
    rawVoltageCreationUrl = ''

    def __init__(self, rawVoltageCreationUrl):
        self.rawVoltageCreationUrl = rawVoltageCreationUrl

    def createRawVoltage(self, startDate: dt.datetime, endDate: dt.datetime) ->RawVoltageCreationResp:
        """create derived voltage using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            RawVoltageCreationResp: Result of the rawVoltage creation operation
        """        
        createRawVoltagePayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.rawVoltageCreationUrl,
                            json=createRawVoltagePayload)
        # print(res)
        # print(type(res))
        # print(res.status_code)
        # print(res.get_json())
        
        operationResult: RawVoltageCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create rawVoltage...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                print(resJSON['message'])
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
                # print(res.text)
        return operationResult