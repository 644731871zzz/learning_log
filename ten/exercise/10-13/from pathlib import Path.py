from pathlib import Path
import json

while True:
    username=input("please talk me your name : ")
    choose=input(f"{username} is  your name? y or n")
    if choose=='y':
        path=Path(f'{username}.json')
        if path.exists():
            try:
                contents=path.read_text()
                user_info=json.loads(contents)

                print(f"name: {user_info['name']}")
                print(f"year: {user_info['year']}")
                print(f"gender: {user_info['gender']}")
            except json.JSONDecodeError:
                print("the file format is incorrect")


        else:
            human_information={}
            human_information['name']=input("what is your name? : ")
            human_information['year']=input("how old art you? : ")
            human_information['gender']=input("what is your gender? : ")

            contents=json.dumps(human_information)
            path.write_text(contents)
            print("been writing")
    elif choose=='n':
        continue
    else:
        print("please talk me true name")
        continue
