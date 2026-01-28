class Employee:
    
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    def get_info(self):
        print('employyee name:', self.name, 'the body is of {} years'.format(self.bond))
    
e=Employee(30000, "John", 2)  # Creating an object of Employee class with constructor
print(e.get_salary())  # Calling the method get_salary on the object e
print(e.get_info())  # Calling the method get_info on the object e