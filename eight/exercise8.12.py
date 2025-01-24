def show_person_toppings(*toppings):
    print("this is your toppings: ")
    for topping in toppings:
        print(f"- {topping}")

show_person_toppings('a','b','c')
show_person_toppings('a')
show_person_toppings('a','b')