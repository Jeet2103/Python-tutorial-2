from functools import reduce
list1=[a for a in range(0,51)]
print(list1)
filter_func= filter(lambda x: x%3==0 and x%5==0,list1)
filter_res= list(filter_func)
print("The numbers between 0 to 50 which is divisable by both 3 and 5 is :  ",filter_res)
list2 = [a for a in range(1,21)]
print(list2)
map_func= map(lambda a : a**2,list2)
map_res= list(map_func)
print("The square of all elements between 1 to 20 is : ",map_res)
list3=[]
for i in range(5):
    i=int(input(f"Num{i+1} : "))
    list3.append(i)
print(list3)
reduce_func= reduce(lambda a,b : a*b,list3)
print(f"The product of all numbers in list {list3} is {reduce_func}")