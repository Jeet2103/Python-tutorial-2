for i in range(7):
    print(i)
else:
    print("Sorry this is not in the loop")
# We can use else statement in for loop and while loop as well as in if-else statement
i=0
while i<11:
    print(f"The value of {i} is {i}")
    if i==6:
        break
    i=i+1
else:
    print("This is not in the loop")
# If i use break statement in any loop then this also braek from else statement.
print(" Go in the loop")
for i in range(11):
    print(" The value is {}".format(i+1))
else:
    print("else block in for loop")
print("Out from the loop")