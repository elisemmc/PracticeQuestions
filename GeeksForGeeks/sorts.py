import sys
import math 

def selectionSort(arr):
# Traverse through all array elements 
    for i in range(len(arr)): 
        
        # Find the minimum element in remaining 
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                
        # Swap the found minimum element with 
        # the first element		 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    return arr

def bubbleSort(arr):
    swapFlag = True # If any of the elements of the array had to be swapped

    while swapFlag:
        swapFlag = False
        # Traverse through all array elements 
        for i in range( len(arr)-1 ):

            if arr[i] > arr[i+1]:
                swapFlag = True
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr

def insertionSort(arr):
    # Traverse through each item in the list
    for i in range( 1, len(arr) ):
        if arr[i] < arr[i-1]:
            # Find where to insert in sorted portion of list
            for j in range(i):
                if arr[i] < arr[j]:
                    arr.insert(j, arr[i])
                    break
    return arr

def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    midPoint = math.ceil(len(arr)/2)
    left = arr[:midPoint]
    right = arr[midPoint:]
    return _merge(mergeSort(left), mergeSort(right))

def _merge(a, b):
    retVal = []
    for _ in range( len(a) + len(b) ):
        if len(a) == 0:
            return retVal + b
        elif len(b) == 0:
            return retVal + a
        elif a[0] < b[0]:
            retVal.append(a.pop(0))
        else:
            retVal.append(b.pop(0))
    return retVal

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    leftArr, rightArr = [], []
    for x in arr[1:]:
        if x <= pivot:
            leftArr.append(x)
        else:
            rightArr.append(x)

    # print(leftArr, pivot, rightArr)
    return quickSort(leftArr) + [pivot] + quickSort(rightArr)

if __name__ == '__main__':
# Driver code to test above 
    A = [64, 25, 12, 22, 11] 
    print(f'SelectionSort: {selectionSort(A)}')
    print(f'BubbleSort: {bubbleSort(A)}')
    print(f'InsertionSort: {insertionSort(A)}')
    print(f'MergeSort: {mergeSort(A)}')
    print(f'QuickSort: {quickSort(A)}')