sqsum = 0
sumsq = 0
for i in range(1, 101):
    sumsq = sumsq+i
    sqsum = sqsum+(i*i)

sumsq = sumsq*sumsq
print("sumsq:", sumsq, "sqsum:", sqsum)
print("diff:", sumsq-sqsum)
