def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    answers = []
    lastAnswer = 0
    for i in queries:
        if i[0] == 1:
            idx = ((i[1] ^ lastAnswer)%n)
            arr[idx].append(i[2])
        else:
            idx = ((i[1] ^ lastAnswer)%n)
            lastAnswer = arr[idx][i[2] % len(arr[idx])]
            answers.append(lastAnswer)
    return answers