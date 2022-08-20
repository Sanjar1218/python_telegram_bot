from telegram import User

class Message:
    def __init__(self, **kwargs) -> None:
        for param, default in kwargs.items():
            setattr(self, param, kwargs.get(param, default))
    
    def newFromJsonDict(data):
        """Convert message object to Dict
        Returns:
            dict: dictionary of message data
        """
        if 'from' in data:
            user = User.newJsonFromDict(data['from'])
        else:
            user = None
        
        if 'chat' in data:
            chat = User.newJsonFromDict(data['chat'])
        else:
            chat = None
        
        
        return Message(
            message_id = data.get('message_id'),
            user = user,
            chat = chat,
            text = data.get('text')
        )
