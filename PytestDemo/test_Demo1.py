import pytest


@pytest.mark.smoke
def test_firstProgram1():
    print("Hello Smruti")

def test_secondProgram():
    print("How are you?")

def test_firstmessage():
    msg="Hello"
    assert msg == "Hello"