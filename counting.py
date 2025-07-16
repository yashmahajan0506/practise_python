str1 = input("Enter a string:")
substring = input("Enter a substring to count the occurrences of it in the string:")
count = 0
for i in range(len(str1) - len(substring)):
    if str1[i:i+len(substring)] == substring:
        count += 1
print(f"The substring '{substring}' occurs {count} times in the string '{str1}'.")


# # st1="yash is yash yash "

# # print(len(st1))
# # substring="yash"

# # count=0

# # # for i in range(len(st1) - len(substring)):
# """
#         i= 18 - 4= 16 
#         ifstr[i:i+len(sustring)==substring]:
#             17:17 +4 ==4:
#                 17:21==4:

#                     count+=1

# """

st1=input("Enter the string:")

subs=input("Enter the substring to find string")

count=st1.count(subs)

print(count)
