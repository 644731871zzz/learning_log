prompt="\ntell me something i can repeat it back to you"
prompt+="\nenter 'quit' to end the program.: "

message=""
while message!="quit":
    message=input(prompt)
    if message !="quit":
        print(message)