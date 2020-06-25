def classify(number):
    if (number < 1):
        raise ValueError("Only natural numbers are allowed.")
    else:
        aliquot_sum = 0

        for i in range(1, int(number/2)+1):
            if number%i == 0:
                aliquot_sum += i
    
        if aliquot_sum == number:
            return "perfect"
        elif aliquot_sum > number:
            return "abundant"
        else:
            return "deficient"
