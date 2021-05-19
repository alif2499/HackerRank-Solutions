

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            add = 0
            add = ar[i]+ar[j]
            if add % k == 0:
                count += 1
    return count


