#DECORATORS
def greet(fx):
    def mfx():
        print("Hello Sir ! \nGood Morning")
        fx()
        print("Thanks for visiting")
    return mfx
@greet
def introduction():
    a= input("Please input your name :  ")
    print(a)

introduction()