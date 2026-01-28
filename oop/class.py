#class : class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

#object : An object is an instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.

class Employee:
    company="HP"
    
    def get_salary(self):
        return 30000

e=Employee()  #an object of class Employee
print(e.get_salary()) #employee object calling the method get_salary