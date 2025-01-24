alien_0={'x_position':0,'y_position':25,'speed':'m1','dodel':'ddddel'}
print(f"original position:{alien_0['x_position']}")

if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print(f"new position {alien_0['x_position']}")

print(alien_0)
del alien_0['dodel']
print(alien_0)