a= input("Please input the string : ")
words = a.split(" ")
nword = []
nword1 = []
res=[]
print("1. code"
      "\n0. decode")
coding = int(input("Enter what you want to do : "))
if coding==1:
    print("The secret code is : ")

    for word in words:
        b = word[0]
        if len(word)<=3:
            c= word[::-1]
        else:
            c =("ABC"+word[1:]+b+"DEF")
        res= nword.append(c)
    print(" ".join(nword))
elif coding==0:
    print("The actual word of this secret code is :")
    for word in words:
        if len(word)<=3:
            nword1.append(word[::-1])
        else:
            d = word[-4]
            e=d+word[3:-4]
            nword1.append(e)
    print(" ".join(nword1))