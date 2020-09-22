from src.errors.custom_error import CustomError


class AuthenticationError(CustomError):
    def __init__(self, reason="Authentication required"):
        self.reason = reason

    @property
    def status_code(self):
        return 403

    def serialize_errors(self):
        return [{"message": self.reason}]
