

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def getTotalX(a, b):
    # Write your code here
    firstArray = a[0]
    lengthA = len(a)
    for i in range(1,lengthA):
        firstArray = (a[i]*firstArray)/gcd(a[i],firstArray)
    if len(b) == 1:
        hcf = b[0]
    else:
        hcf = gcd(b[0],b[1])
        lengthB = len(b)
        for i in range(2,lengthB):
            hcf = gcd(hcf,b[i])
    #print(int(firstArray))
    #print(hcf)
    multiple = firstArray
    count = 0
    i = 1
    while multiple<=hcf:
        if hcf % multiple == 0:
            print(int(multiple))
            count += 1
        i += 1
        multiple = firstArray*i
    return count


