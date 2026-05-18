class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    

e=Employee("John Doe", 50000)
e.project = 6
print(e.project)