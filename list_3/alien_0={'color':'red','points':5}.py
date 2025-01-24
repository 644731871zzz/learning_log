aliens=[]
for alien_number in range(30):
    new_alien={'color':'red','points':15,'speed':'slow'}
    aliens.append(new_alien)
print(aliens[:5])
for alien in aliens[:5]:
    print(alien)

print('\n')

for alien in aliens[:3]:
    if alien['color']=='red':
        alien['color']='yellow'
        alien['points']=20
        alien['speed']='meduim'
    elif alien['color']=='yellow':
        alien['color']='green'
        alien['points']=30
        alien['speed']='fast'
for alien in aliens[:5]:
    print(alien)