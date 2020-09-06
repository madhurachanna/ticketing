class RequestValidationError(Exception):
    errors = []

    def __init__(self, errors):
        self.errors = errors

    @property
    def status_code(self):
        return 400

    def serialize_errors(self):
        return list(
            map(
                lambda err: {"message": err["msg"], "field": err["loc"][0]},
                self.errors,
            )
        )
