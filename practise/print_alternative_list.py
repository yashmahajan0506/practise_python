x = ['Cat', 'tiger', 'Lion', 'leopard', 'bear'] 
y = ['Sparrow', 'parot','peacock','owl','nightingale'] 

#  [‘Cat’, ‘Parrot’, ‘Lion’, ‘Owl’, ‘Bear’]
res=[]
for i in range(len(x)):
    if i %2==0:
        res.append(x[i])
    else:
        res.append(y[i])

print(res) 
