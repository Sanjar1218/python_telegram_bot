import requests


class Bot:
    def __init__(self, token, base_url=None) -> None:
        if base_url==None:
            self.base_url = 'https://api.telegram.org/bot%s' % token 
        else:
            self.base_url = base_url+token

    def getMe(self):
        url = '%s/getMe' % self.base_url

        r = requests.get(url)
        return r.json()
    
    def sendMessage(self, chat_id, text):
        url = '%s/sendMessage' % self.base_url

        payload = {
            'chat_id': chat_id,
            'text': text
        }

        r = requests.get(url, params=payload)
        return r.json()
    
    def getUpdates(self):
        url = f'{self.base_url}/getUpdates'

        r = requests.post(url)

        return r.json()
    
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

