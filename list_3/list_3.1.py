partner=['bob','soonpy','james']
print(f"this is my partner.i invite them.they are :{partner}")
print(f"but {partner[0]} can't come here.because he want to see his son")
partner.pop(0)
partner.insert(0,'olivar')
print(partner)
print(f"i invite a new friend join us ,this is a new list: {partner}")

partner.insert(0,'kinson')
partner.insert(2,'henry')
partner.append('wanye')
print(f"we have a big table we can have si people to have dinner .now they are my si friends.they are:{partner}")

print('sorry,this big table is not come,we can have two people can eat')
friend1=partner.pop()
print(f"sorry {friend1},you should to stay here ,we can to read some books.have a good time")
friend2=partner.pop()
print(f"sorry {friend2},you should to stay here ,we can to read some books.have a good time")
friend3=partner.pop()
print(f"sorry {friend3},you should to stay here ,we can to read some books.have a good time")
friend4=partner.pop()
print(f"sorry {friend4},you should to stay here ,we can to read some books.have a good time")

print(f"but we have tow partner are in the list .they are:{partner}")
print(f"welcome {partner[0]}")
print(f"welcome {partner[1]}")

del partner[0:1]

print(partner,len(partner))