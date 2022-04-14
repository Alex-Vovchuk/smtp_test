class EndpointBaseclass:

    def __init__(self, endpoint_url, method):
        """
        :param endpoint_url: needed service url
        :param method: method of REST API that will be called
        """
        self.method = method

        self.is_set_by_id = None

        self.url = None
        self.base_url = f"{endpoint_url}"

    def build_url(self):
        """
        Firstly we set url, because it could change or modified
        """
        self.url = self.base_url

        """
        Check case when user want to add custom path or id to URL.
        Ex: 
            Before: /member
            After: /member/6789
        """
        if self.is_set_by_id:
            self.url += f"/{self.is_set_by_id}"

    def fetch(self, body=None, cookies=None):
        """
        Fetch method is a last method in this class that prepare all for before sending request.

        :param body: By default it is None. But for POST u can add JSON
        :param cookies: for add cookies :)

        """
        self.build_url()
        result = self.method(url=self.url, body=body, cookies=cookies)

        return result

    def set_by_id(self, object_id):
        """
        Add at the end of url needed params.
        """
        self.is_set_by_id = object_id
        return self

