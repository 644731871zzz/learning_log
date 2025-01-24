from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides=sides
        self.die_number_throws=0
    
    def roll_die(self):
        die_number=randint(1,self.sides)
        print(f"{die_number}")

    

die_6=Die()
while die_6.die_number_throws <10:
    die_6.roll_die()
    die_6.die_number_throws+=1

die_10=Die(10)
while die_10.die_number_throws<10:
    die_10.roll_die()
    die_10.die_number_throws+=1

die_20=Die(20)
while die_20.die_number_throws<10:
    die_20.roll_die()
    die_20.die_number_throws+=1
