#Q)Remove vowels and special characters from a string
import string
s=input("Enter a string ")
table=s.maketrans('','','aeiou.?_!@#$%^&*')
s2=s.translate(table)
print(s2)

#Learning
"""Here's an explanation of the translate() method in Python:

- Purpose:
It's used to modify a string by selectively replacing or removing characters based on a translation table.

- Syntax:
string.translate(table)

table: A translation table, usually created using str.maketrans().
- How It Works:

Create a translation table:
Use str.maketrans(x, y, z) to create a mapping:
x: Characters to replace.
y: Corresponding replacement characters.
z: Characters to delete (made empty in the translation).
Apply the table:
Pass the table to the translate() method on the string.
Each character in the string is looked up in the table and replaced or removed accordingly.
- Example:


- Key Points:
It's often faster than regular expressions for simple character replacements.
It can handle Unicode characters effectively.
It can't change the length of the string (use re.sub() for that).

It's useful for tasks like:
Removing unwanted characters
Encoding/decoding text
Data cleaning
Text normalization
"""