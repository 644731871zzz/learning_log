from car import Car
from electric_car import ElectricCar as EC

my_mustang=Car('ford','mustang','2024')
print(my_mustang.get_descriptive_name())
my_leaf=EC('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())