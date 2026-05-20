class Employye:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def __str__(self):
        return f"{self.name} works in {self.company} and earns {self.salary}"

e=Employye( "John Doe",50000)
print(e.name, e.salary)
print(str(e))