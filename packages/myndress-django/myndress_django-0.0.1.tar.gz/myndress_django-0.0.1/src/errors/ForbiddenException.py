from .BaseException import BaseException

class ForbiddenException(BaseException):
    error = "forbidden"
    description = "Vous n'avez pas le droit d'accéder à cette ressource"
    status = 403