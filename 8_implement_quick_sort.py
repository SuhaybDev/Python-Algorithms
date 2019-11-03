#Function for quick sort
def quickSort(array):
    lenght = len(array)
    if lenght <= 1:
        return array
    else:
        pivot = array.pop()

#Creating 2 lists each for items greater than pivot and items lower than pivot
    items_greater = []
    items_lower = []

#Add items greater than pivot to designated list and the same for items lower than pivot
    for item in array:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

#Returning items_lower, pivot and items_greater with the quickSort function repeatedly running on the lists
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

#Running quickSort function on array
print(quickSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))