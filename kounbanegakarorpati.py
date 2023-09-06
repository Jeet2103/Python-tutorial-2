print("WELCOME KOUN BANEGA KARORPATI")
question= ["1. What is your name ?","What is your father's name?","What is your mother's name?","What is your brother's name?"]
option = ["a. Jeet b. Neel","a. Tulu b. Ambika","a. Tulu b. Neel","a. Ambika b. Neel"]
price = ["0","1000","2000","3000","4000"]
answer = ["a","b","a","b"]
res= []
for i in range (4):
    print(question[i])
    print(option[i])
    res = input()
    if res == answer[i]:
        print(f"You win {price[i+1]} rupees")
    else:
        print("You lose this game .")
        print(f"Your total winning prize is {price[i]}")
        break

