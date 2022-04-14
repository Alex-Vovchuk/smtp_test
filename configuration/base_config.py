from configuration import BASIC_URL


class ConfigBaseclass:
    # This class helps us create different urls for our services. This is done for further expansion.
    BASE_URL = None

    def __init__(self):
        self._url = None

    def _setup_config(self):
        ConfigBaseclass.BASE_URL = f"{BASIC_URL}{self._url}"
