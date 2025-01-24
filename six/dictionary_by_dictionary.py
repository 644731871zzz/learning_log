users={
    'hanghang-jun':{
        'first':'arch',
        'last':'jiang',
        'location':'neimenggu',
    },

    'flippy':{
        'first':'haoqiang',
        'last':'wang',
        'location':'dalian',
    },
}

for username,user_info in users.items():
    print(f"\nUsername : {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\t Full name : {full_name}{user_info['first']}{user_info['last']}")
    print(f"\t Location: {location} {user_info['location']}")
