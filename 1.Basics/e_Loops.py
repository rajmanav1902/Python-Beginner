#for loop
#Used when we know the number of iterations

for i in range(1,6): 
    #Here 6 is exclusive
    print(i*i,end=" ")
print()

#while loop
#Used when we know the terminating condition
i=5
while(i>=1):
    print(i*i,end=" ")
    i=i-1
print()

#To create an infinite loop we can use
# while True