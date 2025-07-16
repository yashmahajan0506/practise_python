#for proper with spacing pattern
def star_pattern(n):
    spaces = n 
    for i in range(1,n+1):
        for j in range(1,spaces+1):
            print(" ",end="")
        for k in range(1,i+1):
            print("* ", end="")
        print()
        spaces = spaces-1
n = int(input("Enter the no of rows you want eneter:"))
star_pattern(n)

#for without space
def star_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()
n = int(input("Enter no of rows:"))
star_pattern(n)

#in reverse
def star_pattern(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("* ", end="")
        print()
n = int(input("Enter no of rows:"))
star_pattern(n)

#for filled square star
side = int(input("Enter no of sides:"))
print("Side filled are:")
for i in range(side):
    for j in range(side):
        print(" *",end='')
    print()