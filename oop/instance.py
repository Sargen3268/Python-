class Employee:
    company = "Asus"
    
    def __init__(self, salary, name, bond , company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company 
    
    def get_salary(self):
        return self.salary
    def get_info(self):
        print('employyee name:', self.name, 'the body is of {} years'.format(self.bond))
    
e=Employee(30000, "John", 2 , "Tesla")  # Creating an object of Employee class with constructor
print(e.company)  # Accessing the company attribute of the object e
print(Employee.company) #class attribute

#object introspection 
print(dir(e))  # This will print all the attributes and methods of the object e