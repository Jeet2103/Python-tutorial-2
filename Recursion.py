def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
print("Factorial of",5, " is ",factorial(5))
def fibonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1)+ fibonachi(n-2)
print("The ",3,"rd term of fibonachi series is :",fibonachi(3))

