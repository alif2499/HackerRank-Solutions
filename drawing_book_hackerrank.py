

def pageCount(n, p):
    # Write your code here
    front = p//2
    back = (n-p)//2
    if p==1 or n==p:
        return 0
    elif n % 2 != 0 and p == n-1:
        return 0
    elif n % 2 == 0 and p == n-1:
        return 1
    return min(front,back)


