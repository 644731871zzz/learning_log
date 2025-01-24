import pytest
from employee import Employee

@pytest.fixture
def staff():
    staff=Employee('','')
    return staff

def test_arch(staff):
    staff.first='arch'
    staff.last='jiang'
    staff.give_raise()
    staff.info()
    assert staff.infoo=="arch jiang 5000"

def test_xuetao(staff):
    staff.first='bai'
    staff.last='xuetao'
    staff.give_raise(6000)
    staff.info()
    assert staff.infoo=="bai xuetao 6000"
