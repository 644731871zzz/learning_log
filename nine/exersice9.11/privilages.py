class Privilages:
    def __init__(self,privileges):
        self.privileges=privileges
    def show_privileges(self):
        print("this is admin can do : ")
        for privilege in self.privileges:
            print(f"{privilege}")   