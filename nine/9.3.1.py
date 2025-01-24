class Car:
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印行驶里程"""
        print(f"this car has {self.odometer_reading}")

    def update_odometer(self,mileage):
        """更新行驶里程"""
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll bake an odometer")

    def increment_odometer(self,miles):
        """让里程表读书增加给定的值"""
        self.odometer_reading+=miles

class ElectricCar(Car):

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery_size=40
    def describe_battery(self):
        """打印电池容量的信息"""
        print(f"this car has a {self.battery_size} - kwh battery")

my_leaf=ElectricCar('nissan','leaf','2024')
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()