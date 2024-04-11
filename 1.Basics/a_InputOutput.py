#This is a single line comment
"""This is a multi 
line comment"""

"""Input is used to take values from user
Output is used to display values in the terminal"""

#input() is used to take user input. It gives default value in string. To take input in different data types 
#use type casting
a=input("Enter the name of a color ")
print("The total number of letters in the color are",len(a))

#print formatting

#To change the line we use \n or """ """
print("Nmaste \nPython")
print("""Namaste
Python""")

#Take input in different data type
a=int(input("Enter an integer"))
print("The square of integer is ",a*a)

#To not change line between consecutive print
print("First Print statement ",end="")
print("Second Print statement")