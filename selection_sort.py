def selection_sort(arr): #[6,5,3,1,8,7,2,4]
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr
        

print(selection_sort([6,5,3,1,8,7,2,4]))
print(selection_sort([1,2,3,4,5,6,7,8]))