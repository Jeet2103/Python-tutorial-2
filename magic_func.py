class num:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return (f"{self.x},{self.y}")
    def __add__(self,other):
        return (f"{self.x+other.x} , {self.y+other.y}")
    def __sub__(self,other):
        return (f"{self.x-other.x} , {self.y-other.y}")
    def __mult__(self,other):
        return (f"{self.x*other.x} , {self.y*other.y}")
    def __div__(self,other):
        return (f"{self.x/other.x} , {self.y/other.y}")
    def __gt__(self,other):
        return (self.x>other.x and self.y>other.y)
    def __lt__(self,other):
        return (self.x<other.x and self.y<other.y)
    def __eq__(self,other):
        return (self.x==other.x and self.y==other.y)
a= num(8,12)
b= num(4,6)
print(f"a = {a}")
print(f"b = {b}")
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mult__(b))
print(a.__div__(b))
print(a.__gt__(b))
print(a.__lt__(b))
print(a.__eq__(b))
print(a+b)

