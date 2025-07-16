# def myfun(*arg):
#     for i in arg:
#         print(arg)

# argv=input("Enter Something:")
# myfun(argv)

# # def number(num):
# #     for i in num:
# #         print(i)
    
# # num=int(input("Enter numbers:"))
# # number(num)
# # # print(num)

def add_numbers(*args):
    result = sum(args)
    print(f"The sum is: {result}")

# Take input from user
user_input = input("Enter numbers separated by space: ")

# Convert input string to list of integers
numbers = list(map(int, user_input.split()))

# Call the function with arbitrary arguments
add_numbers(*numbers)

