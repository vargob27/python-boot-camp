def countdown(a):
    count = []
    for i in range (a+1):
        count.append(a-i)
    return count

def print_and_return(list):
    print(list[0])
    return list[1]


def first_plus_length(list):
    return list[0]+len(list)

def values_greater_than_second(list):
    greater = []
    if len(list) < 2:
        return False
    else:
        for i in range (len(list)):
            if list[i] > list [1]:
                greater.append(list[i])
        print(len(greater))
        return greater

def length_and_value(a,b):
    list = []
    for i in range (a):
        list.append(b)
    return list
