def fibonacci_recursively(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursively(n-1)+fibonacci_recursively(n-2)
    
print(fibonacci_recursively(8))
print(fibonacci_recursively(2))
print(fibonacci_recursively(3))
print(fibonacci_recursively(11))

def fibonacci_iteratively(n):
    arr = [0,1]
    for i in range(2, n+1, 1):
        arr.append(arr[i-2]+arr[i-1])
    return arr[n]


print(fibonacci_iteratively(8))
print(fibonacci_iteratively(2))
print(fibonacci_iteratively(3))
print(fibonacci_iteratively(11))
