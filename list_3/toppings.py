requested_toppings=['mushrooms','extra cheese','green peppers']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni")
if 'extra cheese':
    print("adding extra cheese")

print("\n")

for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("sorry,we are out of green peppers right now")
        #需要注意这里使用else,如果跳过else在for下执行,将会依旧输出三次配料
    else:
        print(f"adding {requested_topping}")
print("\nfinished making your pizza")

print("\n")

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"add {requested_topping}")
    print("\nfinished making your pizza")
else:
    print("are you sure you want a plain pizza?")