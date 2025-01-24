arch={
    'first':'arch',
    'last':'jiang',
    'location':'chifeng',
}
flippy={
    'first':'haoqiang',
    'last':'wang',
    'location':'dalian',
}
simpson={
    'first':'xuetao',
    'last':'bai',
    'location':'beijing',
}

peoples=[arch,flippy,simpson]

for people in peoples:
    first_name=people['first']
    last_name=people['last']
    full_name=f"{first_name} {last_name}"
    location=people['location']
    print(f"Fullname: {full_name}")
    print(f"Location: {location}")
    print("\n")