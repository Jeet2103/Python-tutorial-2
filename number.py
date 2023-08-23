attempt = 1
numbers = []
while attempt<=3:
    count = int(input ("Enter positive number less than 16 :"))
    if count<=16:
        break
    else:
        print("Error...")
        attempt+=1
    if attempt>3:
        print("Maximum limit exceed . ")
        exit()

for i in range(count):
    number = int(input())
    numbers[i:i+1] = [number]
    print("Next?")
max = min = numbers[0]
for i in numbers:
    
    if i>max:
        max=i
for i in numbers:
    
    if i<min:
        min =i

print(numbers[0:1],max,min)