strings = ["apple", "apricot", "app"]

common_chars = set(strings[0] )

for s in strings[1:]:
    common_chars = common_chars & set(s)  

print("Common characters:", common_chars)
