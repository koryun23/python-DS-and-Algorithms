numbers = [4,0,15,0,1,0,12,2,51,6,0,9,13]
def counting_sort(arr): 
    count = [0 for i in range(max(numbers)+1)] 
    output = [0 for i in range(len(arr))] 

    for i in range(len(arr)):
        count[arr[i]]+=1

    for i in range(1,len(count)):
        count[i] += count[i-1]


    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output

print(counting_sort(numbers))
