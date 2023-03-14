import pytest
from tut2.myapp.sample import validate_age


def test_validate_age_valid_age():
    validate_age(2)


# should not fail since we already have an exception specified in the code
def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)


# does not raise the error because 1>0, so this test should fail
def test_validate_age_invalid_age2():
    with pytest.raises(ValueError):
        validate_age(1)