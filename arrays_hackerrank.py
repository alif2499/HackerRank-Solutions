

n = int(input())
arr = list(map(int, input().rstrip().split()))
ar = []
for i in range(len(arr)-1,-1,-1):
    ar.append(arr[i])
print(*ar)