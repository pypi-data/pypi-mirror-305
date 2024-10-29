from .BaseException import BaseException

class MissingParameterException(BaseException):
    error = "missing_parameter"
    status = 400

    def __init__(self, parameter):
        self.parameter = parameter  
        self.description = "Cette requête nécessite le paramètre '{}'".format(parameter)
        super().__init__()
