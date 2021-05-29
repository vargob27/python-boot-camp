import random
def randint(min=0, max=100):
    if min > max:
        min, max = max, min
    num = random.random() * (max - min) + min
    num = round(num)
    return num
