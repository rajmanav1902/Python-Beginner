#Q)Given a string.Find the length of string excluding spaces

s=input("Enter the string ").strip()#Return a copy of the string with leading and trailing whitespace removed.
s=s.replace(" ","")
print(s)
print(len(s))

#Learning

#Ways to remove whitespaces from a string in python
"""strip() method 
replace() method
translate() method
Split the string into words and join without spaces
Regular expression(regex)"""

"""strip() methods:
strip(): Removes leading and trailing whitespace.
lstrip(): Removes leading whitespace only.
rstrip(): Removes trailing whitespace only."""
text = "  Hello, world!  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

"""replace() method:
Replaces specific whitespace characters with empty strings."""
text = " Hello, world!   "
text_without_spaces = text.replace(" ", "")
print(text_without_spaces)

"""translate() method:
Removes all whitespace characters using a translation table.
 How It Works:
Create a translation table:
Use str.maketrans(x, y, z) to create a mapping:
x: Characters to replace.
y: Corresponding replacement characters.
z: Characters to delete (made empty in the translation).
Apply the table:
Pass the table to the translate() method on the string.
Each character in the string is looked up in the table and replaced or removed accordingly."""
import string
text = "   Hello, \tworld! \n "
text_without_spaces = text.translate(str.maketrans('', '', string.whitespace))

"""Splitting and joining:
Splits the string into words, removes extra spaces, and joins back together."""
text = "   Hello,  world!   "
text_without_spaces = " ".join(text.split())

""" Regular expressions:
Uses patterns to match and remove whitespace."""
import re
text = "   Hello,  world!   "
text_without_spaces = re.sub(r"\s+", "", text)

