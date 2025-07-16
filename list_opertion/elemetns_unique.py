def check_elements_unique(my_list):
    a=mylist[0]
    b=mylist[1]
    c=mylist[2]

    if a==b or b==c or a==c:
     print("false")
    else:
        print("true")
# print(a,b,c)
mylist=[( 1,2),(1,2),(1,3)]
check_elements_unique(mylist)

