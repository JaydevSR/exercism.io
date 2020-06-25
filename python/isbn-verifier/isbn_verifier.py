def is_valid(isbn):
    valids = '0123456789X'
    digit_lst = [ i for i in isbn if i in valids ]

    if len(digit_lst) == 10:

        if 'X' in digit_lst:
            if 'X' is digit_lst[-1]:
                digit_lst[-1] = 10
            else:
                return False
        
        sum = 0
        for i in range(10):
            sum += int(digit_lst[i])*(10-i)
        if sum % 11 == 0:
            return True
            
    return False
