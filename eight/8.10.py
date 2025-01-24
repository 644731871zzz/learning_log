messages=['give','me','guita']
sent_messages=[]

def show_list(message_list):
    print("\nthis is the messages : ")
    for message in message_list:
        print(f"{message}")

def send_messages(messages,sent_messages):

    while messages:
        sent_message=messages.pop()
        sent_messages.append(sent_message)
        print(f"{messages}")
        print(f"{sent_messages}")



show_list(messages)
show_list(sent_messages)
print("\n")
send_messages(messages,sent_messages)
print("\n")
show_list(messages)
show_list(sent_messages)