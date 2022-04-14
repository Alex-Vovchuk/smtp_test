from configuration.base_config import ConfigBaseclass


class OneMemberConfig(ConfigBaseclass):

    def __init__(self):
        super().__init__()

        self._url = "/member"
        self._setup_config()
