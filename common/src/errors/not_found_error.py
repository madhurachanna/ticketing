from .custom_error import CustomError


class NotFoundError(CustomError):
    def __init__(self, reason="Not found!"):
        print(reason)
        self.reason = reason

    @property
    def status_code(self):
        return 404

    def serialize_errors(self):
        return [{"message": self.reason}]