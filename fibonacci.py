

n = 10
ar = [0,1]
for i in range(2,n):
    ar.append(ar[i-2] + ar[i-1])
print(*ar)

