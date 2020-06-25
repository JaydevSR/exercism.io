def slices(series, length):
    sr_lst = []
    if length <= 0 or length > len(series):
        raise ValueError("Invalid Length!")
    else:
        for i in range(len(series)-length + 1) :
            sr_lst.append(series[i:(i+length)])
    return sr_lst

