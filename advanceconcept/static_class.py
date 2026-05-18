class Employye:
    company="Google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def print_info(self):
        info = f"{self.name} works in {self.company} and earns {self.salary}"
        print(info)
    
    
    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

e1=Employye("John Doe",50000)
e2=Employye("Jane Doe",60000)


# print(Employye.company)

# e1.print_info()
# e2.print_info()
# print(e2.sum(5,23))
e1.print_company()
e1.change_company("Microsoft")
e1.print_company()