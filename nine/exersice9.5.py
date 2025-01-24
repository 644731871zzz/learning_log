class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0

    def describe_user(self):
        print(f"firstname: {self.first_name}  lastname : {self.last_name}")
    def greet_user(self):
        print(f"welecome to here {self.first_name} {self.last_name}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0


arch=User('Arch','Jiang')
flippy=User('Flippy','Wang')
simpson=User('Simpson','Bai')

arch.describe_user()
arch.greet_user()

flippy.describe_user()
flippy.greet_user()

simpson.describe_user()
simpson.greet_user()

print(f"{arch.first_name} {arch.last_name} try to login :{arch.login_attempts}")
arch.increment_login_attempts()
arch.increment_login_attempts()
arch.increment_login_attempts()
print(f"{arch.first_name} {arch.last_name} try to login :{arch.login_attempts}")
arch.reset_login_attempts()
print(f"{arch.first_name} {arch.last_name} try to login :{arch.login_attempts}")
