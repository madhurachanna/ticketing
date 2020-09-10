class JwtTokenValidationError(Exception):

    def __init__(self, reason='authentication required'):
        self.reason = reason

    @property
    def status_code(self):
        return 403

    def serialize_errors(self):
        return [{"message": self.reason}]
