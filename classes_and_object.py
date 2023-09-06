#CLASSES AND OBJECT
class person:
    name="Jeet"
    occupation="Boss"
    income=10000000000
    def info(self):
        print(f"Name : {self.name}\nOccupation : {self.occupation}\nIncome : {self.income}")
a=person()
b=person()
c=person()
b.name= "Neel"
b.occupation= "Boss 2"
b.income= 100000000000
c.name= "Soumyajit"
c.occupation= "Manager"
c.income= 1000000000
a.info()
b.info()
c.info()
