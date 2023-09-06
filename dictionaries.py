dict1 = { 122:"Jeet Nandigrami",123:"Neel Nandigrami",124:"Pratyush Palit",125: "Soumyajit Dutta"}
print(dict1)
print(dict1[123])
print(dict1[125])
print(dict1[122])
print(dict1.keys())
print(dict1[124])
# print(dict1[128])     # It's shows error because 128 is not a key of dict1
print(dict1.get(125))
print(dict1.get(189))
   # It's do not show error . it shows none if any key is not present in the dictionary.
print(dict1.values())
for key in dict1.keys():
    print(f"The value of corresponding {key} is {dict1[key]}")
print(dict1.items())
for key,value in dict1.items():
    print(f"The name of roll number {key} is {value}")
dict2={126:"Joy Tahashildar",127:"Asmita Sen",128: "Dyuti Dasgupta"}
dict1.update(dict2)
print(dict1)
# dict1.clear()
# print(dict1)
dict1.pop(123)# Using for remove the key order
print(dict1)
dict1.popitem()# Using for remove the last key order
print(dict1)
# del dict1 # For delete the dictionary
print(dict1)
del dict1[126]
print(dict1)
del dict1['122']# Shows error because 122 is ot a string
print(dict1)


