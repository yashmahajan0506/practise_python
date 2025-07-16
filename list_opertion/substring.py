def tocheck_substring(string_list):
    subs='f'
    for i in string_list:
        if subs in i:
            print("true")
            break
        else:
            print("false")
            break
string_list=['apple','bananan','grape']
tocheck_substring(string_list)