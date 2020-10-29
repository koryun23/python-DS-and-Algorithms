def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    rev = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            rev.append(right[right_index])
            right_index += 1
        else:
            rev.append(left[left_index])
            left_index +=1
        if left_index == len(left):
            return rev + right[right_index:]
        elif right_index == len(right):
            return rev + left[left_index:]

print(merge_sort([6,5,3,1,8,7,2,4]))