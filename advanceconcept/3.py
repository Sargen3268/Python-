class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l= self.name.split(" ")
        print(l)
        return l[0]

e=Employee("John Doe", 50000)
print(e.first_name())