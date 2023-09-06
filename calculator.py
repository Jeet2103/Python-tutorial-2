a= int (input("Enter the first number : "))
b= int (input('Enter the second number : '))
if a>b:
    max = a
    min = b
else:
    max = b
    min = a
print("The addition of a and b is : ",(max+min))
print("The substraction of a and b is : ",(max-min))
print("The multipication of aand b is : ",(max*min))
print("The dividation of a and b is : ",(max/min))
print(" The intiger value of (a/b) is : ",(max//min))
print(" The value a to the power b is : ",(max**min))
print("The reminder of (a/b) is : ",(max%min))

