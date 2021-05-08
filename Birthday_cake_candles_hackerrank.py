
arr = [4,2,3,4]
maximum = 0
count = 0
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum = arr[i]
for i in range(len(arr)):
    if arr[i] == maximum:
        count+=1
print(count)


    