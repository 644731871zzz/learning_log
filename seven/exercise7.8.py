sandwich_orders=['tuna','pastrami','chicken','pastrami','veggie','ham','turkey','pastrami']
finished_sandwiches=[]

while sandwich_orders:

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    finishing_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(finishing_sandwich)
    print(f"i made your {finishing_sandwich} sandwich")

print("they are finished making sandwiches : ")
for sandwich in finished_sandwiches:
    print(f" - {sandwich} sandwich")