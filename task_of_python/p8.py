
for i in range(20):
    if i<=0:
        print("Please enter the correct number")
    else:
        num = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                num = 0
                break
        if num:
            print(f"The number {i} is a prime number")