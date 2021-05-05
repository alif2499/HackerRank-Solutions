
#The logic in here is correct but gets a timeout error. Needs to optimize the code



cost = [1, 4, 5, 3, 2]      #[2, 2, 4, 3]
money = 4
n = len(cost)
value = []
for i in range(n-1):
    for j in range(i+1,n):
        if cost[i]+cost[j]==money:
            value.append(i+1)
            value.append(j+1)
print(*value)