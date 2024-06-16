def remove_duplicates(string):
    empty_list = []
    string_1 = string.split()
    for word in string_1:
        if word not in empty_list:
            empty_list.append(word)
    result = " ".join(empty_list)
    return result
string = "i can go to chennai and i can go to madurai"
print(remove_duplicates(string))
