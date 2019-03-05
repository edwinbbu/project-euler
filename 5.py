# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
p = 1
l = [2, 3, 5, 7]
for item in l:
    p = p*item
print(p)
i = 1
while(i < 11):
    if(p % i != 0):
        print("i:", i, "p:", p)
        p = p*i
    print(p)
    i = i+1

# issue with answer
