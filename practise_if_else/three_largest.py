num1=int(input("Enter the number one:"))
num2=int(input("Enter the number two:"))
num3=int(input("Enter the number three:"))

if num1>num2 and num1>num3:
    print(f"Number {num1} is greater")
elif num2>num1 and num2>num3:
    print(f"Number {num2} is greater")
elif num3>num1 and num3>num1:
    print(f"Number {num3} is greater")

