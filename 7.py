import math
n=100001
def isPrime(x):
    sq=math.sqrt(x)
    if(x<=1):
        return False
    else:
        for i in range(2,int(sq)+1):
            if(x%i==0):
                return False
        return True
count=2
a=[2,3]
for j in range(5,200010):
    if(isPrime(j)):
        a.append(j)
        count=count+1
print('count:',count)
print('a:',a)
