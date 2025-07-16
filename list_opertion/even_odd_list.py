def even_odd_list():
    list1=[5,2,9,1,7,8,6]
    even_set={num for num in list1 if num %2==0}
    odd_set={num for num in list1 if num %2!=0}
    print(even_set)
    print(odd_set)
even_odd_list()




# even_set=set()
# odd_set=set()

# for i in list1:
#     if i%2==0:
#         even_set.add(i)
#     elif i%2!=0:
#         odd_set.add(i)
        



