# For loop

print("This is for sting.")
name= "Jeet nandigrami"
for i in name:
    print(i)
print("This is for list")
colours = ["Red","Blue","Green","Black","Yellow"]
for colour in colours:
    print(colour)
    for char in colour:
        print(char)
print("This is for numbers")
for j in range(21):
    print(j)
print("range in the range")
for k in range(5,11):
    print(k)
print("Using step function")
for l in range(1,101,10):
    print(l)

# While loop
print("While loop")
a=0
while(a<21):
    print(a)
    a= a+1
# A while loop programme
print("1. Continue             0. Exit")
b=int(input())

while(b==1):
    c= int(input("Enter the number : "))
    print("Your number is :",c)
else:
 print("You don't want to continue..............")