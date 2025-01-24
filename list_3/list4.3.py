number20=[a for a in range(1,21)]
print(number20)

number1000000=[]
for value in range(1,1000001):
    number1000000.append(value)
print(number1000000)
print(min(number1000000),max(number1000000),sum(number1000000))

number19=[]
for value in range(1,21,2):
    number19.append(value)
print(number19)

number3=[value for value in range(3,31,3)]
print(number3)

number33=[]
for value in range(1,11):
    number33.append(value**3)
print(number33)

number233=[b**3 for b in range(1,11)]
print(number233)