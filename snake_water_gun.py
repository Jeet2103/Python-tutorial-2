import random
comp = random.randint(0,2)
user = int (input("0. SNAKE         1. WATER        2. GUN\nINPUT :  "))
def check(comp,user):
    if (comp==user):
        return 0
    if (comp==0 and user ==1):
        return -1
    if (comp==1 and user==2):
        return -1
    if (comp==2 and user==0):
        return -1
    else:
        return 1
print("USER INPUT ---> ",user)
print("COMPUTER INPUT ---> ",comp)
if check(comp,user)==0:
    print("The match is draw.")
elif check(comp,user)==-1:
    print("Damn ! You are a looser.")
elif check(comp,user):
    print("Congratulation ! You Win.")