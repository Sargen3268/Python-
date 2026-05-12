class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sum(self , p):
        return Point(self.x +p.x, self.y + p.y)
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
    
    def __add__(self, p):
        return Point(self.x +p.x, self.y + p.y)
    
p1 = Point(2, 3)
p2 = Point(4, 5)

p= p1 + p2 #returns a new point 
p.print_point()