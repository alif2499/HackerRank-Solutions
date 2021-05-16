

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appleCount = 0
    orangeCount = 0
    for i in apples:
        distance = 0
        distance = a + i
        if distance >= s and distance <= t:
            appleCount += 1
    for i in oranges:
        distance = 0
        distance = b + i
        if distance >= s and distance <= t:
            orangeCount += 1
    print(appleCount)
    print(orangeCount)


