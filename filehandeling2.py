f= open('myfile.txt','r')
i=0
while True:
    i=i+1
    line = f.readline()# This function can read that file and sequencely print that line
    if not line:
        break
    m1= int(line.split(",")[0])
    m2= int(line.split(",")[1])
    m3= int(line.split(",")[2])
    print(f"Marks of student {i} in subject math is {m1*2}")
    print(f"Marks of student {i} in subject physics is {m2*2}")
    print(f"Marks of student {i} in subject chemistry is {m3*2}")
    print(f"The cgpa of student{i} is {((m1+m2+m3)/3*6)/10}")
    print ("The type of m1 is ",type(m1))
    print("\n")
f1= open("myfile2.txt","w")
lines= ["line1\n","line2\n", "line3"]
f1.writelines(lines)
f1.close()
