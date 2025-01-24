class Restaurant:
    """"""
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_restaurant(self):
        print(f"this {self.type} is good")
    def open_restaurant(self):
        print(f"this {self.name} is opening")

class IceCreamStand(Restaurant):
    """继承类Restaurant,"""
    def __init__(self,name,type,flavors):
        super().__init__(name,type)
        self.flavors=flavors
    def read_flavor(self):
        print(f" flavor is {self.flavors}")

mixuebingcheng_flavors=['caomei','pingcuo','putao','aoliao']
mixuebingcheng_icecream=IceCreamStand('mixuebingcheng','bingqilin',mixuebingcheng_flavors)
mixuebingcheng_icecream.describe_restaurant()
mixuebingcheng_icecream.open_restaurant()
mixuebingcheng_icecream.read_flavor()