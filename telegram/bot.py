import requests

from telegram import User, Update, Message

class Bot:
    def __init__(self, token, base_url=None) -> None:
        if base_url==None:
            self.base_url = f'https://api.telegram.org/bot{token}'
        else:
            self.base_url = base_url+token

    def getMe(self):
        """A simple method for testing your bot's auth token.
        Returns:
          A telegram.User instance representing that bot if the
          credentials are valid, None otherwise.
        """
        url = f'{self.base_url}/getMe'
        r = requests.get(url)
        return User.newJsonFromDict(r.json())
    
    def sendMessage(self, chat_id, text):
        """Use this method to send text messages.
        Args:
          chat_id:
            Unique identifier for the message recipient — telegram.User or
            telegram.GroupChat id.
          text:
            Text of the message to be sent.
        Returns:
          A telegram.Message instance representing the message posted.
        """
        url = f'{self.base_url}/sendMessage'

        payload = {
            'chat_id': chat_id,
            'text': text
        }

        r = requests.get(url, params=payload)
        return Message.newFromJsonDict(r.json()['result'][-1])
    
    def getUpdates(self):
        url = f'{self.base_url}/getUpdates'

        r = requests.post(url)

        return Update.newFromJsonDict(r.json()['result'][-1])
    
    def _requestUrl(self, url, method, data=None):
        """Request an URL.
        Args:
          url:
            The web location we want to retrieve.
          method:
            Either POST or GET.
          data:
            A dict of (str, unicode) key/value pairs.
        Returns:
          A JSON object.
        """
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

