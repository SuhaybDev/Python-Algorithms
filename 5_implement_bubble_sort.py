def bubbleSort(arr):
    n = len(arr)
 
    # Iterate through all array elements
    for x in range(n):
        for y in range(0, n-x-1):
 
            # Interchange places if the element found is greater than the one next to it
            if arr[y] > arr[y+1] :
                arr[y], arr[y+1] = arr[y+1], arr[y]


array = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]


# Call bubbleSort function on array
bubbleSort(array)
# Print sorted array
print (array)
 