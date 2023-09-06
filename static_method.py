def add(a,b):
    return a+b
class math:
    def __init__(self,num):
        self.num= num
    def add_num(self,n):
        self.num = self.num+n
        return self.num
    @staticmethod # Use for when i want to set a method in the class
    def add(a,b):
        return a+b
a= math(10)
print(a.num)
print(a.add_num(6))
print(a.num)
print(f"The addition result of {2} and {3} is {a.add(2,3)}")
print(add(10,78))
