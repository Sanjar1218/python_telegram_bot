import requests

from telegram import User, Update, Message

class Bot:
    def __init__(self, token, base_url=None) -> None:
        if base_url==None:
            self.base_url = f'https://api.telegram.org/bot{token}'
        else:
            self.base_url = base_url+token

    def getMe(self):
        url = f'{self.base_url}/getMe'
        r = requests.get(url)
        return User.newJsonFromDict(r.json()['result'])
    
    def sendMessage(self, chat_id, text):
        url = f'{self.base_url}/sendMessage'

        payload = {
            'chat_id': chat_id,
            'text': text
        }

        r = requests.get(url, params=payload)
        return Message.newFromJsonDict(r.json())
    
    def getUpdates(self):
        url = f'{self.base_url}/getUpdates'

        r = requests.post(url)

        return Update.newFromJsonDict(r.json())
    
    def _requestUrl(self, url, method, data=None):
        if method == 'post':
            try:
                return requests.post(url, data=data)
            except:
                return 'Error'
        elif method == 'get':
            try:
                return requests.get(url, data=data)
            except:
                return 'Erorr'

