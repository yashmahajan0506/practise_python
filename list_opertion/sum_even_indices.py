def sum_even_list():
    list1=[1,2,4,4,6,8,9,1]
    sum_even_position=0
    for i in range(len(list1)):
        if i %2==0:
            sum_even_position=sum_even_position+list1[i]
    print(sum_even_position)          

print(sum_even_list())
 