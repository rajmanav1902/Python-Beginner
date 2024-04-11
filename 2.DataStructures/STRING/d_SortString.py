#Sort a given string in ascending and descending order
s=input("Enter the string")
l=list(s)

l.sort() # Or use asc=sorted(l)
s1="".join(l)

l.sort(reverse=True) #Or use desc=sorted(l,reverse=true)
s2="".join(l)

print("The sorted string in ascending order is",s1)
print("The sorted string in descending order is",s2)

"""
sorted() is generally preferred for smaller lists.
list.sort() is more efficient for larger lists as it avoids creating a new list."""