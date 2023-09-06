with open("myfile.txt","r")as f:
    print(type(f))
    f.seek(9)# From which character I want to print.
    print(f.tell())# Position of seek
    data=f.read(5)#Read the next 5 character
    print(data)
    with open("myfile2.txt","w") as f1:
        f1.write("Hello Jeet")
        f1.truncate(5) # To decide how many character I want in the file.
    with open("Myfile2.txt","r") as f2:
        f2.read() 