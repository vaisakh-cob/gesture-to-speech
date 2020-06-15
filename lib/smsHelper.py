import requests
import json

class Sms4India():
    def __init__(self):
        self.URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        self.apiKey = ''
        self.secretKey = ''

    def sendPostRequest(self, phoneNo: str, textMessage: str):
        """
        This function sends a REST API call to the SMS4INDIA Api to send a message to the phone number provided
        """
        req_params = {
        'apikey': self.apiKey,
        'secret': self.secretKey,
        'usetype':'stage',
        'phone': phoneNo,
        'message': textMessage,
        'senderid':'SMSIND'
        }
        return requests.post(self.URL, req_params)