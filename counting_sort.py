numbers = [4,0,0,1,0,12,2,4,5,1,6,378924,0,9,13,15]
def counting_sort(arr): 
    count = [0 for i in range(max(numbers)+1)]
    output = [0 for i in range(len(arr))]
    #1. fill count array
    for i in range(len(arr)):
        count[arr[i]]+=1
        
    
    #2.modify count array
    for i in range(1,len(count)):
        count[i] += count[i-1]

    
    
    #3. fill output array
    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output

print(counting_sort(numbers))
