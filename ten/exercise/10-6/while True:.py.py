while True:
    #输入一个数并判断
    a=input("give me a number ,i can add the next number : (or 'q' to quit)")
    if a=='q':
        break
    try:
        a=int(a)
    except ValueError:
        print("you give me this a is wrong")
        continue

    b=input("give the nxet number:  (or 'q' to quit)")
    if b=='q':
        break
    try:
        b=int(b)
    except ValueError:
        print("the b number is wrong")
        continue

    c=a+b
    print(f"{a}  +  {b}  =  {c}")