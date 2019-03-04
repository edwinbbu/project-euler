import math
n = 600851475143
sq = math.sqrt(n)
print(sq)
a = []
if n % 2 == 0:
    a.append(2)
for i in range(3, int(sq)+1, 2):
    while(n % i == 0):
        a.append(i)
        n = n/i
print(max(a))
