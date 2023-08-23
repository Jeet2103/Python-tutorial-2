def add(a,b):
    print( a+b)
v=str(add(2,3))

with open ("file.txt",'w') as f:
    f.write("Hello World!")
a= open("file.txt","r")
text= a.read()
print(text)
a.close()
a=open("file.txt",'a')
a.write(v)
a.close()