def max_profit(start,end,arr,max_p):
    if end-start <= 1:
        max_p += max(arr[start],arr[end])
        return max_p
    leftmost = max_profit(start+2,end,arr,max_p+arr[start])
    rightmost = max_profit(start,end-2,arr,max_p+arr[end])
    if leftmost > rightmost:
        return leftmost
    return rightmost

numbers = [20,40,30,60,20,60]
print(max_profit(0,len(numbers)-1,numbers,0))