from name_function import get_formatted_name

print("enter 'q' at any time to quit.")
while True:
    first=input("\nplease give me a first name : ")
    if first=='q':
        break
    last=input("please geve me a last name : ")
    if last=='q':
        break

    formatted_name=get_formatted_name(first,last)
    print(f"\t neatly formatted name : {formatted_name}")