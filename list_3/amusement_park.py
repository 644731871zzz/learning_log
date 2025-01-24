age=1
if 2<age<=4:
    print("your child admission cost is $0")
elif 4<age<18:
    print("you child admission cost is $25")
else:
    print("you child admission cost is $40")

print("\n")

age=5
if age<=4:
    price=0
elif age<18:
    price=25
else:
    price=40
print(f"you child admission cost ${price}\n")

age=13
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20
print(f"you admission cost ${price}\n")


age=3
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20
print(f"you admission cost ${price}")
