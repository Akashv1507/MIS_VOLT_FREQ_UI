import requests
import datetime as dt


class DerivedFrequencyDisplayHandler():
    derivedFrequencyDisplayUrl = ''

    def __init__(self, derivedFrequencyDisplayUrl):
        self.derivedFrequencyDisplayUrl = derivedFrequencyDisplayUrl

    def displayDerivedFrequency(self, startDate: dt.datetime, endDate: dt.datetime)-> dict:
        """display derived Frequency using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            DerivedFrequencyDisplayResp: Result of the derivedFrequency display operation
        """        
        createDerivedFrequencyPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.derivedFrequencyDisplayUrl,
                            json=createDerivedFrequencyPayload)
        # print(res)
        # print(type(res))
        # print(res.status_code)
        # print(res.get_json())
        
        operationResult = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to display derivedFrequency...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                # print(resJSON['message'])
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
                # print(res.text)
        return operationResult