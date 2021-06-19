

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    #keylength = len(keyboards)
    #drivelength = len(drives)
    maxspend = []
    flag = False
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                maxspend.append(i+j)
                flag = True
    if flag == False:
        return -1
    else:
        return max(maxspend)


