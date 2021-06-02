

# Finding n-th fibonacci number
print("Enter a number: ")
n = int(input())
first = 1
second = 1
temp = 0
for i in range(3,n+1):
    temp = second
    second = first+second
    first = temp
print(second)

