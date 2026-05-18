class Employye:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def print_info(self):
        info = f"{self.name} works in {self.company} and earns {self.salary}"
        print(info)
e1=Employye("John Doe",50000)
e2=Employye("Jane Doe",60000)


# print(Employye.company)

e1.print_info()
e2.print_info()
