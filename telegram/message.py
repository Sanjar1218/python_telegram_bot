from telegram import User

class Message:
    def __init__(self, **kwargs) -> None:
        for param, default in kwargs.items():
            setattr(self, param, kwargs.get(param, default))
    
    def newFromJsonDict(data):
        if 'from' in data:
            user = User.newJsonFromDict(data['from'])
        else:
            user = None
        
        if 'chat' in data:
            chat = user.newJsonFromDict(data['chat'])
        else:
            chat = None
        
        
        return Message(
            message_id = data.get('message_id'),
            user = User.newJsonFromDict(data),
            chat = chat,
            text = data.get('text')
        )
