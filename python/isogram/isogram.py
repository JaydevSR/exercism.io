def is_isogram(string):
    flag = True
    str_list = list(string.lower())
    for i in range(len(string)-1):
        s = str_list.pop()
        if s in str_list and s != ' ' and s != '-':
            flag = False
    return flag
