baibai={
    'type':'cat',
    'owner':'lily',
}
snoopy={
    'type':'dog',
    'owner':'chenglu',
}
panda={
    'type':'dog',
    'owner':'emily',
}

pets=[baibai,snoopy,panda]

for pet in pets:
    pet_type=pet['type']
    pet_owner=pet['owner']
    print(f"Type: {pet_type}   Owner:{pet_owner}")
