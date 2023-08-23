def gcd(a,b):
    # rem = a%b
    
    while (a%b)!=0:
        rem = a%b
        a=b
        b= rem
    return b
print("..ok..")
print(gcd(34,9))