ar = [1,4,2,3]
arr = []
start = len(ar) - 1
for i in range(start,-1,-1):
    arr.append(ar[i])
print(*arr)

