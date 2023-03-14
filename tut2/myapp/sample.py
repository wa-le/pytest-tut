

def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be less than 0, but yours is {age}")