ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
arOne = []
n = 9
pair_count = 0

for i in range(len(ar)):
    count = 0
    for j in range (len(ar)):
        if ar[i]==ar[j] and ar[i] not in arOne:
            count += 1
        else:
            continue
    arOne.append(ar[i])
    pair_count += (count//2)
        
print(pair_count)