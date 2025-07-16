def diff_sum(list1):
        
        a,b,c=list1
        z1=a[0]+a[1]
        z2=b[0]+b[1]    
        z3=c[0]+c[1]
        res={z1,z2,z3}
        print(res)
    
list1=[(1,2),(3,4),(5,6)]
print(diff_sum(list1))