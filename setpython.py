# Set is like list .They are mutable but the elements in set is nonrepeatable.
a= { 2,45,3,2,7,8}
print(a)
# void set
b= set()
print(type(b))
for elements in a:
    print(elements)
set1 = {"Jeet" ,3,34,56,"Power"}
set2 = {"Neel",14,18,35,56,"Power"}
print(set1.union(set2))
set1.update(set2)
print(set1,set2)
sets=set1.intersection(set2)
print(sets)
print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set2.issubset(set1))
print(set1.difference(set2))
set1.remove("Power")# remove shows the error if the element is not present in the set
print(set1)
set1.discard("Jeet")
print(set1) # discard do not shows error.
sets2= set1.pop()
print(sets2)
sets3 = set1.pop()
print(sets3)
del set1
print(set1)# As there have no set 1 ......bcz i delete this set
set2.clear()
print(set2)

