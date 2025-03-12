import pytest


@pytest.mark.usefixtures("setup")
class Test_Example:
    def test_fixDemo(self):
        print("First method")
    def test_fixDemo1(self):
        print("Second method")
    def test_fixDemo2(self):
        print("Third method")
