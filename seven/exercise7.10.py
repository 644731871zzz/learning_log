visit_places={}

visit_activing=True
while visit_activing:
    name=input("\n what is your name ? : ")
    place=input("tell me your want to go favorite place : ")

    visit_places[name]=place

    repeat=input("would you like to let another person respond ? (yes/no) ")
    if repeat=='no':
        break

print("--- poll results---")
for name,place in visit_places.items():
    print(f"{name} want to go {place}")


