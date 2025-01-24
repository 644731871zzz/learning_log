from pathlib import Path
import json

def greet_user():
    """询问用户并打印出信息,如果没有让用户创建"""
    username=input("tell me your name : ")
    confirmation=input(f"this {username} is your name? 'y' or 'n'")

    if confirmation=='y':
        path=Path(f'{username}.json')
        if path.exists():
            try:
                contents=path.read_text()
                user_info=json.loads(contents)
                print(f"name {user_info['name']}")
                print(f"year {user_info['year']}")
                print(f"gender {user_info['gender']}")
            except json.JSONDecodeError:
                print("the file format is incorrect")
        else:
            get_new_user_info(username)
    elif confirmation=='n':
        greet_user()
    else:
        print("please input y or n ")
        greet_user()

def get_new_user_info(username):
    user_info={
        'name':username,
        'year':input('how old are you? '),
        'gender':input('what is your gender? ')
    }
    path=Path(f'{username}.json')
    contents=json.dumps(user_info)
    path.write_text(contents)
    print("your information has been saved")

greet_user()

    



