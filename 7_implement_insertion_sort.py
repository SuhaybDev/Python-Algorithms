# Import everything from array module
from array import *

# Get array inputs from user

arr = []

n = int(input("Enter the lenght of the array: "))
for k in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
 
# Function for insertion sort
def insertionSort(arr): 
  
    # Iterate from 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements that are greater than key to one position ahead  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

# Call insertionSort function on arr
insertionSort(arr)
# Print sorted array
print(arr)
 
 

