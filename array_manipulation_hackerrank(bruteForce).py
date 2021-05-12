def arrayManipulation(n, queries):
    # Write your code here
    arr = [0]* n
    for i in queries:
        for j in range(i[0]-1,i[1]):
            arr[j] = arr[j] + i[2]
    return max(arr)