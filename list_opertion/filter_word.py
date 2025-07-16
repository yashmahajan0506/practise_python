def filter_word():
    list1=["apple","is","a","fruit"]
    len_alpha=4
    for i in list1:
        if len(i) < 4 :
           list1.remove(i)
        else:
          print(i)

filter_word()