people={
    'first_name':'Arch',
    'last_name':'Jiang',
    "age":'24',
    'city':'Shanghai'
    }
print(people)

print("\n")

favorite_numbers={
    'jam':1,
    'kan':5,
    'pom':6,
    'kiin':22,
    'nig':11,
    
    }
print(favorite_numbers)

print("\n")

python_term={
    'if':'代表了判断,安端后面的语句是否真,为真则执行',
    'reverse()':'反向打印列表',
    '.srot()':'是方法,用于进行累表的永久排序.使用.sort(reverse=Ture),进行倒叙排序',
    'range()':'使用range(1,9)生成1-8的数',
    '.get()':'使用.get("1","2")来调用字典中的键的值,没有不会报错,将会是提示无或第二段',
}
print(f"'if' can do this: \n {python_term['if']}")

print("\n")

for key_1 in people.keys():
    print(f"key is :{key_1}")
for velue_1 in people.values():
    print(f"values is :{velue_1}")