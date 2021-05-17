

def bonAppetit(bill, k, b):
    # Write your code here
    n = len(bill)
    anna = 0
    for i in range(n):
        if i != k:
            anna += bill[i]
    anna/=2
    if anna == b:
        print("Bon Appetit") 
    else:
        print(int(b - anna)) 

