st = 'thequickbrownfoxjumpsoverthelazydog'
empty=[]
count=0
for i in st:
    if i in empty:
        cnt=st.count(i)
        print(cnt)