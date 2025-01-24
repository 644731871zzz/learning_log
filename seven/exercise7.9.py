sandwich_orders=['tuna','pastrami','chicken','pastrami','veggie','ham','turkey','pastrami']
finished_sandwiches=[]

print("sorry, the deli has run out of pastrami:")

while 'pastrami' in sandwich_orders:
     sandwich_orders.remove('pastrami')

while sandwich_orders:



    finishing_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(finishing_sandwich)
    print(f"i made your {finishing_sandwich} sandwich")

print("they are finished making sandwiches : ")
for sandwich in finished_sandwiches:
    print(f" - {sandwich} sandwich")