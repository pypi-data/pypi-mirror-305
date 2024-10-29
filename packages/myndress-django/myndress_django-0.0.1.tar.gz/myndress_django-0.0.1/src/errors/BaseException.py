class BaseException(Exception):
    error = "base_exception"
    description = "Une erreur est survenue"
    status = 400

    def __init__(self):
        self.err_args = {
            "detail": self.description,
            "error": self.error,
            "type": "error",
            "status": self.status
        }