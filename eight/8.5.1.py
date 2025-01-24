def make_pizza(size,*toppings):
    """概述要制作的披萨"""
    print(f"\n Making a{size} - inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(18,'mushrooms','greenperpers','extra cheese')