import random
def quicksort(arr, start, stop):
    if(start < stop):
        pivotindex = partitionrand(arr,start, stop)
        #print("pivotindex : ",pivotindex, " Array : ", arr)
        quicksort(arr , start , pivotindex)
        quicksort(arr, pivotindex + 1, stop)
 
def quicksortdet(arr,start,end):
 if (start<end):
    pivotidx=pivotfirst(arr,start,end)
    #print("pivotindex : ",pivotidx, " Array : ", arr)
    quicksortdet(arr , start , pivotidx)
    quicksortdet(arr, pivotidx + 1, end) 
 
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] =arr[randpivot], arr[start]
    print("Pivot : ",arr[start], " After swapping : ", arr)
    return partition(arr, start, stop)

def pivotfirst(arr,start,end):
    print("Pivot : ",arr[start], " Array : ",arr)
    return partition(arr,start,end)
    
def partition(arr, start, stop):
    global res
    pivot = arr[start]
    i = stop+1
    for j in range(stop, start, -1):
        res += 1
        if arr[j] > pivot :
            i -= 1
            arr[j], arr[i] = arr[i], arr[j]
 
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i-1
 
if __name__ == "__main__":
    array1 = list(map(int, input("Enter elements in array : ").split()))
    print("In Randomized quick sort : ")
    res = 0
    quicksort(array1, 0, len(array1) - 1)
    print("No of basic operations : ", res)
    
    print("In deterministic quick sort : ")
    res = 0
    quicksortdet(array1,0,len(array1)-1)
    print("No of basic operations : ", res)
    print(array1)