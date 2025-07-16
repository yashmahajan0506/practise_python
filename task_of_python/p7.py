# Python program to count the number of even and odd numbers from a series of numbers.
numbers=1,2
count=0
cal=0

for i in numbers:
    if i % 2==0:
        count=count+1
    else:
        cal=cal+1    
print("The numbers of Even number is",count)
print("The numbers of Even number is",cal)

