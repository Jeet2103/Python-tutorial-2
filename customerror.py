# This is raising custom error
a= int(input("Enter any number between 10 and 15 : "))
if a<10 or a>15 :
    raise ValueError ("Please enter the value between 10 and 15 ")
# In this way i can create a custom error
b= input("Please enter the 'quit' string : ")
if b!="quit":
    raise ValueError("Yot don't write 'quit' string.")