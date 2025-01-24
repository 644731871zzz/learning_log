cities={
    'tokyo':{
        'country':'japan',
        'population':'3700wan',
        'fact':'this city have most peole'
    },
    'beijing':{
        'country':'chian',
        'population':'2100wan',
        'fact':'this city is chian"s capital'
    },
    'singapore':{
        'country':'singapore',
        'population':'580wan',
        'fact':'this city is a country'
    },
}
for name,values in cities.items():
    print(f"this is the {name} condition:")
    for value in values.items():
        print(f"{value}")