

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
scores = [3, 4, 21, 36, 36, 36, 10, 28, 35, 5, 24, 42]
scores = list(set(scores))
print(scores)
low = 99999
high = 0
low_count = 0
high_count = 0
result = []
length = len(scores)
for i in range(length):
    low = min(low,scores[i])
    high = max(high,scores[i])
    if i > 0 and low == scores[i]:
        low_count += 1
    elif i > 0 and high == scores[i]:
        high_count += 1
result.append(high_count)
result.append(low_count)

print(result)
        

