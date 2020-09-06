import requests
import datetime as dt
from src.typeDefs.derivedVoltageCreationResp import DerivedVoltageCreationResp


class DerivedVoltageCreationHandler():
    derivedVoltageCreationUrl = ''

    def __init__(self, derivedVoltageCreationUrl):
        self.derivedVoltageCreationUrl = derivedVoltageCreationUrl

    def createDerivedVoltage(self, startDate: dt.datetime, endDate: dt.datetime) ->DerivedVoltageCreationResp:
        """create derived voltage using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            DerivedVoltageCreationResp: Result of the derivedVoltage creation operation
        """        
        createDerivedVoltagePayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.derivedVoltageCreationUrl,
                            json=createDerivedVoltagePayload)
        # print(res)
        # print(type(res))
        # print(res.status_code)
        # print(res.get_json())
        
        operationResult: DerivedVoltageCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create derivedVoltage...'
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