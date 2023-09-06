def multipication():
    a= input("Please input the number : ")
    try:
        print(f"The multipication table of {a} is :")
        for i in range(1,11):
            print(f"{int(a)} X {i} = {int(a)*i}")
        return 1
    except:
        print("Invalid inputs................please check ")
        return 0
    finally:
        print("I am always on")
b= multipication()
print(b)
print("The multipication table is over................")
print("The programme is done.")
# Finally always use for when I want to print something , which doesn't matter on try: or except:
try:
    num = int(input("Enter a intiger : "))
    a=[2,3,4,5]
    print(a[num])
except ValueError:
    print("Number is not intiger..............")
except IndexError :
    print("Invalid index................")
