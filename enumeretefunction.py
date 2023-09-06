a= [1,2,34,56,98,100,23]
# This is with out enumerate
index=0
for i in a:
    print(i)
    if index==5:
        print(f"Jeet you doing awsome...{i} marks")
    index+=1
#This is with enumerate
for index,i in enumerate(a):
    print(i)
    if index==5:
        print("You doing a great job Jeet .......")
# If i want to strt index from 1.....
for index,i in enumerate(a,start=1):
    print(i)
    if index==5:
        print("Good job !!")