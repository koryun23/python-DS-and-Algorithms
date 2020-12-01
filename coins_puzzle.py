def max_profit(start,end,arr,max_p):
    if end-start <= 1:
        max_p += max(arr[start],arr[end])
        return max_p
    min_leftmost = min(max_profit(start+2,end,arr,max_p+arr[start]), max_profit(start+1,end-1,arr,max_p+arr[start]))
    min_rightmost = min(max_profit(start,end-2,arr, max_p+arr[end]), max_profit(start+1, end-1, arr, max_p+arr[end]))   
    return max(min_leftmost,min_rightmost)


numbers = [20,40,30,60,20,10]
print(max_profit(0,len(numbers)-1,numbers,0))