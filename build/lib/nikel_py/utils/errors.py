class NoDataFound(Exception):

    def __init__(self, message = "No Data was found for your query"):
        super().__init__(message)


class InvalidKey(Exception):

    def __init__(self, key : str, message = "Invalid Key Passed in: '{}'"):
        self.message = message.format(key)
        super().__init__(self.message)



class ResponseError(Exception):
    def __init__(self, message = "HTTP Request Unsuccessful. Possibly Rate limited?"):
        super().__init__(message)