class Car:
    def __init__(self,make,model,year):
        """初始化汽车的描述"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=20

    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印汽车的里程表信息"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self,mileage):
        """
        修改里程表读书为指定值
        禁止里程表读书回调    
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self,miles):
        """让里程表读数指定增加"""
        if miles>=0:
            self.odometer_reading+=miles
        else:
            print("")


my_car=Car('audi','a4',2024)
print(my_car.get_descriptive_name())

my_car.update_odometer(23_500)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()