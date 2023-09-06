class employee:
    company_name= "Apple"# CLASS VARIABLE
    noOfEmployee = 0
    def __init__(self,name):
        self.name=name
        self.raise_amount= 0.23 # INSTANCE VARIABLE
        employee.noOfEmployee +=1
    def show_details(self):
        print(f"Name :- {self.name}\nRaise Amount :- {self.raise_amount}\nCompany Name :- {self.company_name}\nEmployee Number :- {self.noOfEmployee}\n")
emp1= employee("Jeet")
emp1.show_details()
emp2= employee("Neel")
emp2.show_details()
emp3= employee("Pratyush")
emp3.company_name="Google"
emp3.show_details()
emp4= employee("Asmita")
employee.company_name="Amazon"
emp4.show_details()
emp5= employee("Soumyajit")
emp5.show_details()
