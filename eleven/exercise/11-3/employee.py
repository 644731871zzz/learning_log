class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.salary=0

    def give_raise(self,increase=5000):
        self.salary=increase

    def info(self):
        self.infoo=f"{self.first} {self.last} {self.salary}"
        
