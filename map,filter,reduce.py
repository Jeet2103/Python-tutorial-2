# Map,Filater and Reduce -------> Specially work for itrated function
# MAP
# def cube(x):
#     return x*x*x
l= [1,2,3,4,5,6,7,8,9,10]
# newl=[]
# for items in l:
#     newl.append(cube(items))   # When I want to append any elements in the list
newl1= list(map(lambda x: x*x*x,l))
newl2= list(map(lambda x:(2+x)/2,l))
print(newl1)
print(newl2)
#FILTER
# def filter_function(x):
    # return x>2

from functools import reduce
newnewl= list(filter(lambda x: x>2,l))
print(newnewl)
#REDUCE ---------> Work as a recursion function
numbers= [2,3,4,56,34,569]
sum = reduce(lambda x,y : (x+y),numbers)
print(sum)