def greet_users(names):
    for name in names:
        msg=f"hello, {name.title()}! "
        print(msg)

usernames=['arch','flippy','simpson']
greet_users(usernames)