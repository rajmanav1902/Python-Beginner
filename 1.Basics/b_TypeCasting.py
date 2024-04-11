#Type casting refers to changing the data type of a variable

#Implicit type casting
a=5 #int
b=9.0 #float
c=a+b #int+float=float
print(c," ",type(c))

#Explicit type conversion
a=599
a=float(a)
b=str(a)
print(a," ",type(a))
print(b," ",type(b))