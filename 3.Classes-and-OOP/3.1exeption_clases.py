
def validate(name):
    if len(name)< 10:
        raise ValueError


#validate("joe") #error raised but it's undescribed


""" """
class NameTooShortError(ValueError):
    pass

def validate_prime(name):
    if len(name) < 10:
       raise NameTooShortError(name)


validate_prime("jane")