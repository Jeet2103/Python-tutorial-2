class employee:
    company = "Apple"
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"{self.name} works in {self.company} company")
    @classmethod # That means if I change the instance variable the the class variable will automaticilly change.
    def change_cmpny(cls,new_company):
        cls.company= new_company
emp1= employee('Jeet')
emp1.show()
emp2= employee("Neel")
emp2.change_cmpny("Tesla")
emp2.show()
print(employee.company)