pizzas=['bishengke','dalemei','piqilin']
for pizza in pizzas:
    print(f"my favorite pizza is {pizza}")
print("i like pizza very much.")

friend_pizzas=pizzas[:]
pizzas.append('apple')
friend_pizzas.append('banana')
print("my favorate pizzas are:")
for my in pizzas:
    print(my)

print("\nfriend favorate pizzas are:")
for friend in friend_pizzas:
    print(friend)