banned_users=['ada','eth','sol','bnb']
user_1='ada'
user_2='and'
if user_1 in banned_users:
    print(f"{user_1} is in bannedusers list")

if user_2 not in banned_users:
    print(f"{user_2} is not in bannedusers list")