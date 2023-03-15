import sys
import pytest
from tut3.myapp.sample import add, check_len, sub


def test_add_num():
    assert add(1, 2) == 3


# if our test is throwing some exception, ignore it
@pytest.mark.xfail(sys.platform == "win32", reason="ignore on windows")
def test_add_list():
    assert add([1], [3]) == [1, 3]
    raise Exception()


def test_add_str():
    assert add("a", "b") == "ab"


# ignore test if python version > 3.7
@pytest.mark.skipif(sys.version_info > (3, 7), reason="skipping due to system version")
def test_sub_num():
    assert sub(100, 2) == 98


@pytest.mark.skip(reason="Just skipping for now")
def test_check_len():
    assert check_len([1, 2, 4, 5]) in [2, 3, 4, 6]


# can also run tests using CLASS

class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"

