ar = [1,2,3,4,5,6]
arr = []
rotate = 4
j = 0

for i in range (len(ar)):
    if i + rotate < len(ar):
        arr.append(ar[i + rotate])
    else:
        arr.append(ar[j])
        j += 1
print(arr)