import pytest

from .BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestDataLoad(BaseClass):
    def test_addprofile(self, dataLoad):
        log= self.getlogger()
        log.debug(dataLoad[2])

        print(dataLoad[1])
        print(dataLoad[2])


