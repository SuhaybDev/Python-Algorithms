A = [4, 1, 5, 3, 7]

#Function for merge sort
def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

def mergeSort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        mergeSort2(A, first, middle)
        mergeSort2(A, middle + 1, last)
        mergeSort2(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(99999999999)
    R.append(99999999999)
    i = j = 0

for k in range(first, last+1):
    if L[i] <= R[j]:
        A[k] = L[i]
        i += 1
        
    else:
            A[k] = R[j]
            j += 1
