class UnauthorizedException(Exception):
    code = 401

    def __init__(self, message, code=401, *args):
        super().__init__(args)
        self.message = message
        self.code = code


class FinanceServiceException(Exception):
    message = None
    code = 400

    def __init__(self, message, code=400, *args):
        super().__init__(args)
        self.message = message
        self.code = code


class NotUniqueException(Exception):
    message = None

    def __init__(self, message, *args):
        super().__init__(args)
        self.message = message
