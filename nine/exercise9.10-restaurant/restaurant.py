"""餐厅的主模块"""

class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def print_restaurant(self):
        print(f"{self.name} has {self.type}")