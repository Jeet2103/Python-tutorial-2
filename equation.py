import math
a=int(input())
b=int(input())
c=int(input())
D= (b**2)-(4*a*c)
if D>=0:
    R1 = (-b+math.sqrt(D))/(2*a)
    R2 = (-b-math.sqrt(D))/(2*a)
    print("Roots are :",R1,"and",R2)
elif D<0:
    integer = -b/(2*a)
    complex = math.sqrt(abs(D))/(2*a)
    
    r1=f" {integer} + ({complex})i "
    print("Root1 : ",r1)
    print("Root2 : ",integer," - (",complex,")i ")

