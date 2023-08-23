class  employee:
    def __init__(self,name,designation,salary):
        self.name= name
        self.designation=designation
        self.salary= salary
    def display(self):
        print(f"Name : {self.name}\nDesignation : {self.designation}\nSalary : {self.salary}")

jeet=employee("Jeet","CEO",120000000)
jeet.display()

class students:
    def __init__(self,roll,name,marks1,marks2,marks3) :
        self.roll=roll
        self.name= name
        self.marks1= marks1
        self.marks2= marks2
        self.marks3= marks3
    def display(self):
        
        print(f"Roll : {self.roll}\nName : {self.name}\nTotal marks : {self.marks1 + self.marks2 + self.marks3}")

soumya = students(90,"Soumyajit",89,90,99)
soumya.display()

class person:
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender
class publication:
    def __init__(self,no_rp,no_book,no_art):
        self.no_rp= no_rp
        self.no_book=no_book
        self.no_art= no_art
class faculty(person,publication):
    def __init__(self,name,age,gender,desig,dept,no_rp,no_book,no_art):
        person.__init__(self,name,age,gender)
        publication.__init__(self,no_rp,no_book,no_art)
        self.desig= desig
        self.dept= dept
    def display(self):
        print(f"Name of faculty : {self.name}\n{self.age}\nGender : {self.gender}\nDesignation : {self.desig}\nDepartment : {self.dept}\nNo. of research papers published : {self.no_rp}\nNo. of books chapters published : {self.no_book}\n No. of articles published : {self.no_art}")
        
a= faculty("Jeet",19,"Male",2,3,4,"HOD","CSE")
a.display()