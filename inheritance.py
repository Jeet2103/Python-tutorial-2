class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show_data(self):
        print(f"NAME:- {self.name}\nID:- {self.id}")
class web_developer(employee):
    def web_info(self):
        print("A Web Developer")
class app_developer(employee):
    def app_info(self):
        print("A App Developer")
class pro_level(app_developer):
    def pro_info(self):
        print("A Pro level App Developer")
a=pro_level("Jeet Nandigrami","12")
a.show_data()
a.app_info()
a.pro_info()
b=web_developer("Neel Nandigrami","20")
b.show_data()
b.web_info()

