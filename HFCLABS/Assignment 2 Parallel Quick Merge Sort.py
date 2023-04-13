from multiprocessing import Process, Manager

def parallelQuickSort(arr, left, right):
    if left < right:
        pivotIndex = (left + right) // 2
        pivotValue = arr[pivotIndex]
 
        i = left
        j = right
 
        while i <= j:
            while arr[i] < pivotValue:
                i += 1
            while arr[j] > pivotValue:
                j -= 1
 
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
 
        p1 = Process(target=parallelQuickSort, args=(arr, left, j))
        p2 = Process(target=parallelQuickSort, args=(arr, i, right))
        p1.start()
        p2.start()
        p1.join()
        p2.join()

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
 
        mergeSort(left)
        mergeSort(right)
 
        i = j = k = 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def main():
    # Get the number of elements in the array
    numElements = int(input("Enter the number of elements: "))
 
    # Get the elements of the array
    arr = list(map(int, input("Enter the elements: ").split()))
 
    # Choose the sort type (QuickSort or MergeSort)
    sortType = int(input("Enter 1 for QuickSort or 2 for MergeSort: "))
    if sortType == 1:
        # Perform parallel QuickSort
        parallelQuickSort(arr, 0, numElements - 1)
    else:
        # Perform MergeSort
        mergeSort(arr)
 
    # Print the sorted array
    print("Sorted array:", arr)

if __name__ == '__main__':
    main()