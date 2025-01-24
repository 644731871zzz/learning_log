promt="\nPlease enter the name fo a city you have visited:"
promt+="\n(enter 'quit' when you are finished) "
 
while True:
    city=input(promt)

    if city=='quit':
        break
    else:
        print(f"i love to go to {city.title()}!")