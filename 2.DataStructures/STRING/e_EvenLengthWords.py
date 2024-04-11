#Write a python program to print only even length word
s=input("Enter the string ")
words=s.split()

for word in words:
    if len(word) %2==0:
        print(word)