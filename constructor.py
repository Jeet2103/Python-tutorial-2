# CONSTRUCTOR
class person:
    def __init__(self,name,occupation):# Constructor
        print("Hello! I am a person")
        self.name = name
        self.occupation=occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person("Jeet","Boss 1")
a.info()
b= person("Neel","Boss 2")
b.info()
c=person("Soumyajit","HR")
c.info()
