#Q) Find if a string is palindrome or not
s=input("Enter the string to be checked ")
s1=s[::-1]
print(s==s1)

#Learning

"""
== fis comparison operator. Checks if the value of the variable is same or not
'is' is an identity operator.Checks if the two variables point the same object or not
"""
"""
Ways to reverse a string in python
String slicing: It is used in the code above
reversed() and join()
list comprehension
"""

"""
reversed() and join():
Use reversed() to create a reversed iterator of the string.
Join the characters using join().
"""
text = "Hello, world!"
reversed_text = "".join(reversed(text))
print(reversed_text)

"""
List Comprehension:
Construct a reversed list of characters and join them back into a string.
"""
text = "Hello, world!"
reversed_text = "".join([char for char in text[::-1]])
print(reversed_text)

