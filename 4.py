n = 999
i = n
while (i >= 900):
    print("n:", n, "i:", i)
    k = n*i
    a = str(k)
    r = a[::-1]
    print(a, r)
    if a == r:
        print("true")
        break
        exit(0)
    if(i == 900):
        n = n-1
        i = n+1
    i = i-1
