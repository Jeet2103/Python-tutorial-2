# Lambda Function is a small function.
squre = lambda x : x*x
cube = lambda x:x*x*x
average = lambda x,y,z: (x+y+z)/3
print(squre(5))
print(cube(5))
print(int(average(8,10,3)))
def eqn(fx,value):
    return 10 + fx(value)
print(eqn(squre,9))
print(eqn(lambda x:x*x*x,9))
# So basically lambda is a small function which i can use in any small apply