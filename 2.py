a = 1
b = 2
sum = 2
for i in range(2, 10000):
    c = a+b
    if(c >= 4000000):
        break
    if(c % 2 == 0):
        sum += c
    a = b
    b = c
print(sum)
