
def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence[-1]
        smallItem = []
        greaterItem = []
        for i in range(length-1):
            if sequence[i] < pivot:
                smallItem.append(sequence[i])
            else:
                greaterItem.append(sequence[i])
        return quickSort(smallItem) + [pivot] + quickSort(greaterItem)

print(quickSort([5,6,7,8,9,7,5,6,7,8,5,2,56,43,22]))


