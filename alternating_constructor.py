class employee:
    def __init__(self,name,salary,age):
        self.name= name
        self.salary=salary
        self.age= age
    def show(self):
        print(f"{self.name} get {int(self.salary)} rupees and his age is {int(self.age)}")
    @classmethod # In this way I can make an alternating constructor.
    def fromstr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]),int(string.split("-")[2]))
    @classmethod
    def fromstr1(cls,string):
        name,salary,age = string.split(",")
        return cls(name,int(salary),int(age))
a= employee("Jeet","1000000000000","20")
a.show()
string = "Neel-12000000-12"
b=employee.fromstr(string)
b.show()
string1= "Soumyajit,10000000000,23"
c= employee.fromstr1(string1)
c.show()