class User:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def describe_user(self):
        print(f"firstname: {self.first_name}  lastname : {self.last_name}")
    def greet_user(self):
        print(f"welecome to here {self.first_name} {self.last_name}")

class Admin(User):
    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges=privileges
    def show_privileges(self):
        print(f"this is Admin can do : ")
        for privilege in self.privileges:
            print(f"{privilege}")


admin_privileges=["can add post","can delete post","can ban user"]

Arch=Admin('Arch','Jiang',admin_privileges)
Arch.describe_user()
Arch.greet_user()
Arch.show_privileges()

