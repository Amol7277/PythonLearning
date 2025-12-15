import pytest

@pytest.mark.smoke
def test_method1():@pytest.mark.sanity
def test_login1():
    print("Negative Test")
    assert 1-1 == 2

    print("Positive Test")
    assert 1+1 == 2


@pytest.mark.sanity
def test_login2():
    print("Negative Test")
    assert 1-1 == 2