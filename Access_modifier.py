class student :
    def __init__(self):
        self.__name ="Jeet"
obj = student()
print(obj._student__name)# That's call name miling
# print(obj.__dir__())
class student1:
    def __init__(self):
        self._name="Jeet Nandigrami"
    def _funfact(self):
        return  "Coffie lover"
class subject(student1):
    def _subject(self):
        return  "Web Development"
obj1=student1()
obj2 = subject()
print(obj1._name)
print(f"{obj1._name} is a {obj1._funfact()}")
obj2._name = "Neel Nandigrami"
print(f"{obj2._name} is a specialist of {obj2._subject()}")