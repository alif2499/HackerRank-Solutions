a = [5,6,7]
b = [3,6,10]
result = []
alice = 0
bob = 0

for i in range (len(a)):
    if a[i] < b[i]:
        bob += 1
    elif a[i] > b[i]:
        alice += 1
    else:
        continue
result.append(alice)
result.append(bob)

print(result)