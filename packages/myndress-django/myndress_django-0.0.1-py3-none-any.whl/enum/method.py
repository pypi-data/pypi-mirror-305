from enum import Enum

class Method(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    PATCH = 5
    HEAD = 6
    OPTIONS = 7

    @staticmethod
    def get_method(method):
        if type(method) == Method:
            return method
        if type(method) == str:
            if method.upper() == 'GET':
                return Method.GET
            elif method.upper() == 'POST':
                return Method.POST
            elif method.upper() == 'PUT':
                return Method.PUT
            elif method.upper() == 'DELETE':
                return Method.DELETE
            elif method.upper() == 'PATCH':
                return Method.PATCH
            elif method.upper() == 'HEAD':
                return Method.HEAD
            elif method.upper() == 'OPTIONS':
                return Method.OPTIONS
        else:
            return None