a=int(input("Enter side one:"))
b=int(input("Enter side two:"))
c=int(input("Enter side three:"))

if (a+b >c) and (a+c >b) and (b+c >a):
    print("valid triangl")
else:
    print("Inavalud triangle")