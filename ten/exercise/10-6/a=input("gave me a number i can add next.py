while True:
    #提示用户输入第一个数
    a=input("give me a number to add to the next number(or 'q'o quit) : ")
    if a=='q':
        break

    #尝试输入转化为整数
    try:
        a=int(a)
    except ValueError:
        print("that is not 'a' valid number please enter a number")
        continue

    b=input("give me another number (or 'q' to quit) : ")
    if b=='q':
        break

    try:
        b=int(b)
    except ValueError:
        print("that is  not 'b' valid number please enter a number.")
        continue

    c=a+b
    print(f"the sum of {a} and {b} is: {c}")