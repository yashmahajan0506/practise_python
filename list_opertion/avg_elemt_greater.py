
def elem_greater(mylist):

    lenght=len(mylist)
    sum_value=sum(mylist)
    lenght_value=sum_value//lenght
    print(mylist[lenght_value:])

mylist=[1,2,3,4,5,6]
elem_greater(mylist)



