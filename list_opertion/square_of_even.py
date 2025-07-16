mylist=[1,2,3,4,5,6]
sum=0
for i in mylist:
    if i %2==0:
       sq =i*i
    #    print(sq)
       sum=sum+sq
print(f"sum = {sum}")
