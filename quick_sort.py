numbers = [6,5,3,1,8,7,2,4]
def get_pivot(arr, low, high): 
    pivot_index = high
    i = low
    while i < pivot_index:
        if arr[pivot_index] > arr[i]: 
            i += 1
        else:
            arr[pivot_index], arr[pivot_index-1] = arr[pivot_index-1], arr[pivot_index]
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index -= 1

    return pivot_index
def quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = get_pivot(array, low, high)
        get_pivot(array, low, pi-1)
        get_pivot(array, pi+1, high)
        

for i in range(len(numbers)):
    print(numbers[i])



print(quick_sort(numbers), 0, len(numbers) - 1)

