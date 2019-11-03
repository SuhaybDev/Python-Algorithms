# Import everything from array module
from array import *

# Get array inputs from user

arr = []

n = int(input("Enter the lenght of the array: "))
for k in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
    
# Iterate through all elements of the array 
for i in range(len(arr)): 
    
    # Find the lowest element in unsorted array  
    min_idx = i 
    for j in range(i+1, len(arr)): 
        if arr[min_idx] > arr[j]: 
            min_idx = j 
            
    # Swap the found element with the first element       
    arr[i], arr[min_idx] = arr[min_idx], arr[i] 


# Print sorted array  
print(arr)