# strings are immutable

a= "Jeet Nandigrami is a very good boy .He is the man who can do many things which anyone can't imagine"
a1= "Jeet!!!!!!!!"
print(a.upper())
b= "NEEL NANDIGRAMI IS A VERY BAD BOY. HE IS A SPOILBATT"
print(b.lower())
print(a+b)
print(a.replace("Jeet","Neel"))
d="asmita is mu crush.\n i really want to get her as a life partner"
print(d.capitalize())
print(a1.rstrip("!"))
print(a.split(" "))# convert string to list.
print(a.endswith("imagine"))
print(a.endswith("is",5,18))
print(a.find("is"))
print(b.isupper())
print(a.startswith("Jeet"))