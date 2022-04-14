from configuration.base_config import ConfigBaseclass


class MemberListConfig(ConfigBaseclass):

    def __init__(self):
        super().__init__()

        self._url = "/members"
        self._setup_config()
