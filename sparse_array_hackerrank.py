ar = ["aba", "baba", "aba", "xzxb"]  #string input
arr = ["aba", "xzxb", "ab"]         #queries to be searched
array = []

for i in arr:
    count = 0
    for j in ar:
        if i == j:
            count += 1
    array.append(count)
print(array)