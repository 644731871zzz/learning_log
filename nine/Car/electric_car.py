"""一组表示电动车的类"""

from car import Car

class Battery:
    """电动汽车电池模拟"""
    def __init__(self,battery_size=40):
        self.battery_size=battery_size
    
    def describe_battery(self):
        """打印电池容量信息"""
        print(f"This car has a {self.battery_size} - kwh battery")

    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range=150
        elif self.battery_size == 65:
            range=225

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """模拟电动车独特之处"""
    def __init__(self,make,model,year):
        """先初始化父类属相,再初始化电动车属性"""
        super().__init__(make,model,year)
        self.battery=Battery()

      
        