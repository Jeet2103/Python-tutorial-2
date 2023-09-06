name = ["Jeet","Pratyush","Soumyajit","Joy","Sanglap"]
print(name)
mix = [1,2,3,4,"Jeet","Neel","3.4",6,7,8,467,"nun"]
print(mix)
print(mix[0])
print(mix[1:7])
print(mix[1:-2])# -2 is equal to len(mix) - 2
if "3.4" in mix:
    print("Yes")
else:
    print("No")
if "ee" in "Jeet":
    print("Yes")
else:
    print("No")
print(mix[1:])
print(mix[:5])
print(len(mix))
print(len(name))
print(mix[1:8:2])
print(name[2:-1])
# List manupulating
number = [1,2,5,34,78,2,3,3,3,3,3,]
print(number)
number.append(89)#For add some elements in the list.
print(number)
number.sort()
print(number)
number.reverse()
print(number)
print(number.index(5))# For know the position of  89
print(number.count(3))
m= number
m[4]= 233333
print(number)# number will not change
m1= number.copy()
m1[3]=455555
print(number)# number will not change
print(m1)
number.insert(7,8777777)
print(number)
m2=[677777,766666,899999,9888888]
number.extend(m2)
print(number)
k= m2+number# for merge two or excessive list
print(k)
# Tuppels are same as list. But tupples are not mutable




