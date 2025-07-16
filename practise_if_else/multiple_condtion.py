def mul_con(num):
    if num > 0 and num %2==0:
        print("Number is positive and even:")
 
    elif num < 0 and num %2!=0:
        print("Number is negative and odd:")
    elif num ==0:
        print("Number is zero")
    elif num > 0 and num %2!=0:
        print("Number positive and odd ")
    else:
        print("the number is negative and even ")

num1=int(input("Enter a number:"))
mul_con(num1)
