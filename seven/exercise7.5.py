prompt="tell me your years you know how many money to see movie : "
prompt="tell me 'quit' to quit"

active=True
while active:
    yearsold=input(prompt)
    if yearsold=='quit':
        break
    yearsold=int(yearsold)
    if 0<yearsold<3:
        print("free")
    elif 3<=yearsold<12:
        print("10dollar")
    elif yearsold>=12:
        print("15dollar")
    else:
        print("please tell me true number")