number=input("tell me a number , can tell you this number is even or odd? : ")
number=int(number)
number_10=number%10
if number_10==0:
    print("this number can divisible by 10")
else:
    print("this number cann't divisible by 10")