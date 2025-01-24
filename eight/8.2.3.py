def describe_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print(f"\ni have a {animal_type}")
    print(f"{animal_type}'s name is {pet_name.title()}")

describe_pet('cc','cat')
describe_pet(animal_type='cat',pet_name='cc')
describe_pet(pet_name='cc',animal_type='cat')
describe_pet('dd')