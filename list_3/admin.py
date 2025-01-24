usenames=[]
if usenames:
    for usename in usenames:
        if usename=='admin':
            print("hello admin,would you like to see a status report?")
        elif usename in usenames:
            print(f"hello {usename} ,thank you for logging in again")
        else:
            print("we need some users")
else:
    print("we need some users")


current_users=['bob','ada','tom','lili','wang']
new_users=['bob','dive','thoofo','lili','kinson']
for new_user in new_users:
    if new_user in current_users:
        print("please change you name")
    else:
        print("your name can be used")


current_users_01=[]
for current_user_01 in current_users:
    current_users_01.append(current_user_01.title())
print(current_users_01)
current_users_02=[current_user_02.upper() for current_user_02 in current_users]
print(current_users_02)

print("\n")

numbers=[number for number in range(1,10)]
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number==2:
        print(f'{number}nd')
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")