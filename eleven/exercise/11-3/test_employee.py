from employee import Employee

def test_give_default_raise():
    """是否可以给于标准工资"""
    staff_1=Employee('arch','jiang')
    staff_1.give_raise()
    staff_1.info()
    assert staff_1.infoo=="arch jiang 5000"
    
def test_give_custom_raese():
    """是否可以给予自定义工资"""
    staff_2=Employee('bai','xuetao')
    staff_2.give_raise(6000)
    staff_2.info()
    assert staff_2.infoo=="bai xuetao 6000"