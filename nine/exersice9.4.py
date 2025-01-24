class Restaurant:
    """"""
    def __init__(self,name,type):
        self.name=name
        self.type=type
        self.number_served=0
    def describe_restaurant(self):
        print(f"this {self.name} is good")
    def open_restaurant(self):
        print(f"this {self.name} is opening")
    def set_numver_served(self,people_number):
        self.number_served=people_number
        print(f"now this {self.name} has {self.number_served} peoples")
    def increment_number_served(self,update_people):
        self.number_served+=update_people
        print(f"now this {self.name} has {self.number_served} peoples")
        



cailan_restaurant=Restaurant('Cailan','Yuecai')
dabianlu_restaurant=Restaurant('Dabianlu','Huoguo')
hanbaowan_restaurant=Restaurant('hanbaowan','kuaican')

print(f"this is {cailan_restaurant.name} restaurant")
print(f"this restaurant is cooking {cailan_restaurant.type}")

cailan_restaurant.describe_restaurant()
cailan_restaurant.open_restaurant()

dabianlu_restaurant.describe_restaurant()
hanbaowan_restaurant.describe_restaurant()

cailan_restaurant.set_numver_served(50)
cailan_restaurant.increment_number_served(10)