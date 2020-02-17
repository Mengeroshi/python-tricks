class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass


def validate_prime(name):
    if len(name) < 10:
       raise NameTooShortError(name)

try:
    validate_prime(name)
except BaseValidationError as err:
    handle_validation_error(err)