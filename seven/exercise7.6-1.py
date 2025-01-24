prompt="tell me you want eat what pizza toppings? "
prompt+="use 'quit' to quit: "

topping=''
toppings_all=[]


while topping!='quit':
    topping=input(prompt)

    toppings_all.append(topping)
        
    print(f"now this is your toppings : {toppings_all} ")