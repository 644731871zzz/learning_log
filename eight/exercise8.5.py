def describe_city(city_name='shanghai',city_nation='china'):
    """show this city is in this nathion"""
    print(f"\n{city_name.title()} is in the {city_nation.title()}")

describe_city()
describe_city('new york','america')
describe_city('beijing')