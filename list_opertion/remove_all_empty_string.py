def check_string_empty(mylist):
    empty_list=[]
    
    for i in mylist:
        if i!="":
         
         empty_list.append(i)
    print(empty_list)

mylist=["apple","","banana","grape",""]
check_string_empty(mylist)