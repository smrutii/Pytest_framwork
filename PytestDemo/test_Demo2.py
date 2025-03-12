import pytest


def test_firstProgram1():
    print("Hello Pankaj")

@pytest.mark.xfail
def test_secondProgram4():
    print("How are you?")
print("Script executed")

def test_crossbrowser(crossBrowser):
    print(crossBrowser[1])

