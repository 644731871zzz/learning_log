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

class Batter:
    def __init__(self,battery_size=40):
        """初始化电池的属性"""
        self.battery_size=battery_size
    def describe_battery(self):
        """发音一条电池容量信息"""
        print(f"This car has a {self.battery_size}-kwh battery")
    def get_range(self):
        """打印一条消息,指出电池续航里程"""
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f"this car can go about{range} miles on afull charge")

class ElectricCar(Car):
    """电动汽车独特之处"""
    def __init__(self,make,model,year):
        """先初始化父类的属性,再初始化电动汽车的特有属性"""
        super().__init__(make,model,year)
        self.battery=Batter()

my_leaf=ElectricCar('nissan','leaf','2024')
print(my_leaf.get_descriptive_name)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()