import requests
import datetime as dt
from src.typeDefs.derivedVdiCreationResp import DerivedVdiCreationResp


class DerivedVdiCreationHandler():
    derivedVdiCreationUrl = ''

    def __init__(self, derivedVdiCreationUrl):
        self.derivedVdiCreationUrl = derivedVdiCreationUrl

    def createDerivedVdi(self, startDate: dt.datetime, endDate: dt.datetime) ->derivedVdiCreationResp:
        """create derived Vdi using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            derivedVdiCreationResp: Result of the derivedVdi creation operation
        """        
        createDerivedVdiPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.derivedVdiCreationUrl,
                            json=createDerivedVdiPayload)
        # print(res)
        # print(type(res))
        # print(res.status_code)
        # print(res.get_json())
        
        operationResult: derivedVdiCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create derivedVdi...'
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