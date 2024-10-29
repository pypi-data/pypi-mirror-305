from .BaseException import BaseException

class MethodException(BaseException):
    error = "method_not_implemented"
    description = "Cette méthode n'est pas implémentée"
    status = 405

    def __init__(self, method):
        self.method = method  