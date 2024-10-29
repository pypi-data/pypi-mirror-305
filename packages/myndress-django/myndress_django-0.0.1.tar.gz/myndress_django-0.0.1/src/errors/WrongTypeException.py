from .BaseException import BaseException

class WrongTypeException(BaseException):
    error = "wrong_type_parameter"
    status = 400

    def __init__(self, parameter, expected_type, got_type):
        self.parameter = parameter 
        self.description = "Cette requête nécessite le paramètre '{}' de type '{}', '{}' reçu".format(parameter, expected_type, got_type)
        super().__init__()
