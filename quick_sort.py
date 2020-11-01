numbers = [6,5,3,1,8,7,2,4]
def get_pivot(arr, low, high): 
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(array, low, high):
    if low < high:
        pi = get_pivot(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
    return array
        
print(get_pivot(numbers,0,len(numbers) - 1))
print(quick_sort(numbers, 0, len(numbers) - 1))

