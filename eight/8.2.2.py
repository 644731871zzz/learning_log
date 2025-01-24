def describe_pet(animal_type,pet_name):
    """显示动物信息"""
    print(f"\n i have a {animal_type}.")
    print(f"{animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster',pet_name='cc')
describe_pet(pet_name='cc',animal_type='dog')