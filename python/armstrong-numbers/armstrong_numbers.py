# STRINGS TO THE RESCUE #

def is_armstrong_number(number):
    num_digits = len(str(number))
    sq_sum = 0
    for digit in str(number):
        digit = int(digit)
        sq_sum += digit**num_digits
    return sq_sum==number


    