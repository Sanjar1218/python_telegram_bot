
class User:
    def __init__(self, **kwargs) -> None:
        for param, default in kwargs.items():
            setattr(self, param, kwargs.get(param, default))


    def newJsonFromDict(data):
        return User(
            id = data.get('id', None),
            first_name = data.get('first_name', None),
            last_name=data.get('last_name', None),
            username=data.get('username', None)
        )
