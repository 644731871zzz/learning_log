my_foods=['hamburger','cake','vegetable','apple']
friend_foods=my_foods[:]

my_foods.append('rice')
friend_foods.append('tomato')

print("my favorite foods are:")
print(my_foods)

print("\nmy friend favorite food are:")
print(friend_foods)


print("the first three items in the list are:")
print(my_foods[:3])
for a in my_foods[:3]:
    print(a)

print("the itens from the middle of list are:")
print(my_foods[1:4])
for b in my_foods[1:4]:
    print(b)

print("the last three items in the list are:")
print(my_foods[-3:])
for c in my_foods[-3:]:
    print(c)