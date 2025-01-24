prompt="\n tell me someting ,and i will repeat it back to you "
prompt+="\n enter 'quit' to end the program. "
active = True
while active:
    message=input(prompt)

    if message=='quit':
        active=False
    else:
        print(message)