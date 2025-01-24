"""用来表示汽车的类"""

class Car:
    
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name=f"{self.year} {self.model} {self.make}"
        return long_name.title()
    
    def read_odometer(self):
        """打印出汽车行驶里程"""
        print(f"this car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self,mileage):
        """
        将里程表读书设置为指定值
        拒绝里程表数值回调
        """
        if mileage >= self.odometer_reading :
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self,miles):
        """让里程表增加指定量"""
        self.odometer_reading+=miles

