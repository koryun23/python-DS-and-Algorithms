def binary_search(arr,num): #[3,7,9,13,20,24,29], num = 24
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] < num:
            left = mid+1
        elif arr[mid] > num:
            right = mid-1
        else:
            return mid
    
print(binary_search([3,7,9,13,20,24,29],29))