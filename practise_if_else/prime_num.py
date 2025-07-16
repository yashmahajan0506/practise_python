num=int(input("Enter the Number:"))

if num <=0:
    print("it is not prime number")
else:
    if num ==1:
        print("it is not prime number")
    else:
        for i in range(2,num):
            if num %2==0:
                print("The number is is not prime")
            else:
                print("The number is prime:")
                break
        print("It is prime number ")


