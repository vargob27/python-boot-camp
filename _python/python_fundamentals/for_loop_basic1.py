# for i in range (151):
#     print(i)

# for i in range (5, 1001, 5):
#     print(i)

# for i in range (1, 101, 1):
#     if i % 10 == 0:
#         print("Coding Dojo")
#     elif i % 5 == 0:
#         print("Coding")
#     else:
#         print(i)

# sum = 0
# for i in range (1, 500001, 2):
#     sum+=i
    
# print(sum)

# for i in range (2018, 0, -4):
#     print(i)

# lowNum = 2
# highNum = 9
# mult = 3
# for i in range (lowNum, highNum+1, 1):
#     if i % mult == 0:
#         print(i)

a = 1250000
p = 0
r = .0675
t = 50
n=12

p=(a*(r/n))/(((1+(r/n))**(n*t))-1)
print(p)
print(252*(12*50))
# a = (p*(((1+r)**t) - 1))/r

# print(a)
# b = 3000*40
# print(a-b)