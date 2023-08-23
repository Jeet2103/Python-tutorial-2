def add(a,b):
    return a+b
def decor(add):
    def f(x,y):
        if x<0:
            x=0
        if y<0:
            y=0
        return add(x,y)
    return f
a= decor(add)
print(a(20,3))
print(a(20,-3))
def my_gen():
    n=10
    yield n
    n+=10
    yield n
    n+=100
    yield n

a= my_gen()
print(f"Yield 1 : {next(a)}")
print(f"Yield 2 : {next(a)}")
print(f"Yield 3 : {next(a)}")
