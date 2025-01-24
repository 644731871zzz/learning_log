def person_want():
    """收集用户信息"""

    person_toppings=[]
    want_acting=True
    while want_acting:
        person_topping=input("Tell me what you do want toppings? : ")
        print("if You don't want any topping,you can talk 'q' to quit")
        if person_topping=='q':
            want_acting=False
        else:
            person_toppings.append(person_topping)
    return person_toppings

def show_person_toppings(person_toppings):
    for person_topping in person_toppings:
        print(f" - {person_topping}")


show_person_toppings(person_want())




