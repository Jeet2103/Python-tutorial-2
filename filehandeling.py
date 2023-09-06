#..................Reading mode.........................
# f= open('myfile.txt','r')
# print(f.read())
# f.close()
#.....................Append mode.......................
# f= open('myfile.txt','a')
# f.write("\n Yoy are really very good boy also")
# f.close()
#.....................Write mode........................
with open('myfile2.txt','w') as f:# When I use tis then I don't have to use close() function
    f.write("You are a very bad boy.")
# f.close()