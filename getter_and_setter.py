class my_value:
    def __init__(self,value):
        self.value = value
    def show(self):
        print(f"The value is {self.value}")
    #GETTER
    @property
    def ten_value(self):
        return 10*self.value
    #SETTER
    @ten_value.setter
    def ten_value(self,new_value):
        self.value = new_value/10
obj= my_value(10)
obj.ten_value= 1303
obj.show()
print(obj.ten_value)