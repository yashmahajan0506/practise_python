mylist=['apple','bannana ','grape',"frutie"]

letter='a'
empty_list=[]

for i in mylist:
    if letter in i:
        empty_list.append(i)
    else:
        print("Provide Valid string")
print(empty_list)