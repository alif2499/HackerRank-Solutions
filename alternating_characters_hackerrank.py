


def alternatingCharacters(s):
    # Write your code here
    count = 0
    length = len(s)
    for i in range(length-1):
        if s[i] == s[i+1]:
            count += 1
    return count

