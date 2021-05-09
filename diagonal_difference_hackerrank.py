ar = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]
     
diagOne = 0
diagTwo = 0

for i in range(len(ar)):
    diagOne = diagOne + ar[i][i]
    diagTwo = diagTwo + ar[i][len(ar)-i-1]

difference = diagOne - diagTwo
if difference < 0:
    print(difference*-1)
else:
    print(difference)
print(diagOne)
print(diagTwo)