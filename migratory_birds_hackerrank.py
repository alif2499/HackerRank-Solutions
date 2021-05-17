

from collections import Counter

def migratoryBirds(arr):
    # Write your code here
    list_freq = (Counter(arr))
    maxi = 0
    mini = 9999
    ar = []
    for key, value in list_freq.items():
        maxi = max(value,maxi)
    for key, value in list_freq.items():
        if value == maxi:
            ar.append(key)
    return min(ar)

