def convert(number):
    return_string = ''
    flag = False
    if number % 3 == 0:
        return_string += 'Pling'
        flag = True
    if number % 5 == 0:
        return_string += 'Plang'
        flag = True
    if number % 7 == 0:
        return_string += 'Plong'
        flag = True

    if flag == False:
        return str(number)
    else:
        return return_string
