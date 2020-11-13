def get_pivot(arr, low, high): 
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return i+1
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = get_pivot(arr, low, high)
        quick_sort(arr, low, pivot_index-1)
        quick_sort(arr, pivot_index+1, high)
    return arr

numbers = [6,5,3,1,8,7,2,4]    

# print(get_pivot(numbers,0,len(numbers) - 1))
print(quick_sort(numbers, 0, len(numbers) - 1))

