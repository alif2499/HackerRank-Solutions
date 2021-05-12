def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+2)
    for i in queries:
        a = i[0]
        b = i[1]
        k = i[2]
        arr[a] += k
        arr[b+1] -=k
    length = len(arr)
    sum = 0
    highest = 0
    for i in range(length):
        sum += arr[i]
        highest = max(sum,highest)
    return highest