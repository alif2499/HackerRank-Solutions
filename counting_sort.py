# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def countingSort(arr):
    # Write your code here
    result = [0]*(max(arr) + 1)                 # Initializes array of (max value of the array + 1) zeros
    final = []                                  # Initialize list to store sorted array
    for i in range(len(arr)):                   # Iterate over each element of the array
        result[arr[i]] += 1                     # Increament the value of each position according to the respective positional value from given array
                                                        # Here the result array is used as counter to the occurence of elements in given array
    for i in range(len(result)):                # Iterate over each element of the result array
        if result[i] != 0:                      # If the occurence is not zero, append the index (i) value result[i] times to the (final) array as sorted array
            final.extend([i]*result[i])
    print(final)                                # Prints the sorted array
arr = [1,1,3,2,1]
countingSort(arr)
