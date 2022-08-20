
class User:
    def __init__(self, **kwargs) -> None:
        params_defaults = {
            'id': None,
            'first_name': None,
            'last_name': None,
            'username': None,
        }
        for param, default in params_defaults.items():
            print(param)
            setattr(self, param, kwargs.get(param, default))


    def newJsonFromDict(data):
        print(data)
        return User(
            id = data.get('id', None),
            first_name = data.get('first_name', None),
            last_name=data.get('last_name', None),
            username=data.get('username', None)
        )
