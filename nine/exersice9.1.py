class Restaurant:
    """"""
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def describe_restaurant(self):
        print(f"this {self.name} is good")
    def open_restaurant(self):
        print(f"this {self.name} is opening")


cailan_restaurant=Restaurant('Cailan','Yuecai')
dabianlu_restaurant=Restaurant('Dabianlu','Huoguo')
hanbaowan_restaurant=Restaurant('hanbaowan','kuaican')

print(f"this is {cailan_restaurant.name} restaurant")
print(f"this restaurant is cooking {cailan_restaurant.type}")

cailan_restaurant.describe_restaurant()
cailan_restaurant.open_restaurant()

dabianlu_restaurant.describe_restaurant()
hanbaowan_restaurant.describe_restaurant()