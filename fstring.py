line = "My name is {0} and my brother name is {1}"
name1="Jeet Nandigrami"
name2= "Neel Nandigrami"
print(line.format(name1,name2))
# Using f string
print(f"I am {name1} and {name2} is my brother")
print(f"I am {{name1}} and he is {{name2}}")#When i want to print the variable name in the string
# Doc string............. This have to be below of the function
def square(n):
    # print(n) If below the function there have any command then doc string do not work
    ''' This is a function. Enter the value of n and get the square of n  '''
    print("The square of ",n,"is ", n**2)
square(5)
print(square.__doc__)
# PEP 8 --> Python Enhancement Proposal
import this
#If I import 'this' library then I can see a poem.This call a PEP 8.





