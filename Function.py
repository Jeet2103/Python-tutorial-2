def average(a,b):
    return (a+b)/2

c= int(average(2,6))
print(c)
def addition(a,b):
    pass#for write the body later
     #return a+b
# d= addition(1,9)
# print(d)
def greatest(a,b=91):
    if a>b :
        print(a,"is the greatest number.")
    else:
        print(b,"is the greatest number")
d=int(input("The value of a is : "))
e= int(input("The value of b is : "))
greatest(e)
def average2(*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum/len(number)
res = average2(2,3,4,5,6,7)
print("The result of this number's average is : " ,res)

