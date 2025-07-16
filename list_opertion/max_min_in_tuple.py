def check_max_min(mylist):
    elements=[num for tup in mylist for num in tup ]
    print("Maximum : ",max(elements))
    print("Minimun : ",min(elements))
mylist=[(0,5),(2,8),(7,11),(20,11)]
check_max_min(mylist)

#print(value)
# for i in mylist:
#     for j in i:
#       if j >value:
#        value=j

# print(value)
