def bubble_sort(arr): # 
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                
    return arr
print(bubble_sort([8,7,6,5,4,3,2,1]))
print(bubble_sort([6,5,3,1,8,7,2,4]))
