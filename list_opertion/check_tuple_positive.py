def check_tuple_postive(mylist):
    value=[num for tup in mylist for num in tup]
    #print(value)
    for i in value:
      if i >1:
       print("true")
    else:
        print("false")

mylist=[(1,0),(3,-1)]
print(check_tuple_postive(mylist))


