import pytest


@pytest.fixture(scope="class")
def setup():
    print("Let's Print Something")
    yield
    print("Last method")

@pytest.fixture()
def dataLoad():
    print("Data for user profile")
    return ["Rahul", "Deshpande","Akola"]

@pytest.fixture(params=[("Chrome","Smruti"), ("Firefox","pankaj")])
def crossBrowser(request):
    return request.param