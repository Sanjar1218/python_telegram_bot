from telegram import Message

class Update():
    def __init__(self, **args) -> None:
        for param, default in args.items():
            setattr(self, param, args.get(param))
        
    
    def newFromJsonDict(data):
        return Update(
            update_id = data.get('update_id'),
            message = Message.newFromJsonDict(data['message'])
        )