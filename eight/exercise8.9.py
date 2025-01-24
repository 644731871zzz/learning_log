def pass_list():
    messages=['give','me','guita']
    return messages
def show_list(message_list):
    print("\nthis is the messages : ")
    for message in message_list:
        print(f"{message}")


show_list(pass_list())