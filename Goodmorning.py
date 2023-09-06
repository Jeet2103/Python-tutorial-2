import time
timestamp = time.strftime('%H:%M:%S')
datestamp = time.strftime('%dth %B, %Y')
print(timestamp)
print(datestamp)
hour=  int (time.strftime('%H'))
minute =  int (time.strftime('%M'))
second =int (time.strftime('%S'))
year = int (time.strftime('%Y'))
if hour==12 and minute==00 and second==00:
    print("Good Noon sir")
elif hour>=12 and hour<18 and minute>0:
    print("Good Afternoon sir ")
elif hour>=18 and hour<=23:
    print("Good Evening sir")
else:
    print("Good Morning Sir")
if year%4==0 and year % 100 !=0 :
    print(" The year is leap-year")
elif year % 400 == 0:
    print("The year is leap-year")
else:
    print("The year is not leap-year")
# Match case
a= int(input("Please enter the number : "))


match a:
    case 0:
        print("Your statement is false.")
    case 1:
        print("Your statement is true.")
    case _:
        print("The number is ",a)
