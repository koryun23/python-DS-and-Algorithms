def perms(arr,first):
    if first == len(arr) - 1:
        print(arr)
        return
    if first == len(arr) - 2:
        print(arr)
        arr[first],arr[first+1] = arr[first+1],arr[first]

perms([1,2,3,4],0)
