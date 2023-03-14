from tut1.myapp.sample import add, check_len


def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


def test_check_len():
    assert check_len([1, 2, 4, 5]) in [2, 3, 4, 6]


# can also run tests using CLASS

class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"


