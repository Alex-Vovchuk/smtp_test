import requests


class MethodsBaseClass:
    @staticmethod
    def get(**kwargs):
        return requests.get(
            kwargs.get('url'),
            headers=kwargs.get('headers'),
            cookies=kwargs.get('cookies'),
            )

    """
    POST method I add for example to show grows possibility
    """
    @staticmethod
    def post(**kwargs):
        return requests.post(
            kwargs.get('url'),
            json=kwargs.get('body'),
            headers=kwargs.get('headers'),
            cookies=kwargs.get('cookies'),
            )


