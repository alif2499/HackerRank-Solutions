


def makeAnagram(a, b):
    # Write your code here
    a_freq = {}
    for i in a:
        if i in a_freq:
            a_freq[i] += 1
        else:
            a_freq[i] = 1
    
    count = 0
    for i in b:
        if i in a_freq:
            if a_freq[i]>0:
                a_freq[i] -= 1
            else:
                count += 1
        else:
            count += 1
    total = sum(a_freq.values())
    
    return count+total

