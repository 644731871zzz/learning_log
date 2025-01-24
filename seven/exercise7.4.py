prompt="tell me you want eat what pizza toppings? "
prompt+="use 'quit' to quit: "
toppings_all=[]
while True:
    topping=input(prompt)
    oppings_all=[]

    if topping=='quit':
        break
    else:
        toppings_all.append(topping)
        
        print(f"now this is your toppings : {toppings_all} ")