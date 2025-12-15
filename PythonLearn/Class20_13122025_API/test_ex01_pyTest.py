import pytest

@pytest.mark.smoke
def test_method1():
    print("Positive Test")
    assert 1+1 == 2

@pytest.mark.sanity
def test_method2():
    print("Negative Test")
    assert 1-1 == 2
