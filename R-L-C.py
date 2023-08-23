import math
r= int(input())
l= int(input())
c= int(input())
f= int(input())
XL = 2*math.pi*f*l
XC = 1/(2*math.pi*f*c)
X= XL-XC
I = math.sqrt((r**2)+(X**2))
print("XL = ",XL)
print("XC = ",XC)
print("I = ",I)


