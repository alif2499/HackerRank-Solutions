# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def countingSort(arr):
    # Write your code here
    result = [0]*(max(arr) + 1)
    final = []
    for i in range(len(arr)):
        result[arr[i]] += 1
    for i in range(len(result)):
        if result[i] != 0:
            final.extend([i]*result[i])
    print(final) 
arr = [1,1,3,2,1]
countingSort(arr)