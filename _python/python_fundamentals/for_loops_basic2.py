def biggie_size(list):
    for i in range (len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

def count_positives(list):
    count = 0
    for i in range (len(list)):
        if list[i] > 0:
            count += 1
    list[len(list)-1] = count
    return list

def sum_total(list):
    sum = 0
    for i in range (len(list)):
        sum += list[i]
    return sum

def average(list):
    avg = 0
    sum = 0
    for i in range (len(list)):
        sum += list[i]
    avg = sum / len(list)
    return avg

def length(list):
    listLength = len(list)
    return listLength

def minimum(list):
    if len(list)==0:
        return False
    min = list[0]
    for i in range (len(list)):
        if list[i] < min:
            min = list[i]
    return min

def maximum(list):
    if len(list)==0:
        return False
    max = list[0]
    for i in range (len(list)):
        if list[i] > max:
            max = list[i]
    return max

def ultimate_analysis(list):
    if len(list)==0:
        return False
    sum = 0
    avg = 0
    minimum = list[0]
    maximum = list[0]
    length = len(list)
    for i in range (len(list)):
        sum += list[i]
        if list[i] < minimum:
            minimum = list[i]
        if list[i] > maximum:
            maximum = list[i]
    avg = sum / len(list)
    dict = {"sumTotal": sum, "average": avg, "minimum": minimum, "maxmimum": maximum, "length": length}
    return dict

def invertList(list): 
    for i in range(len(list)//2): 
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list
