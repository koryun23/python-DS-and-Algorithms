def fibonacci_recursively(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursively(n-1)+fibonacci_recursively(n-2)
    
print(fibonacci_recursively(8))
print(fibonacci_recursively(2))
print(fibonacci_recursively(3))
print(fibonacci_recursively(11))

def fibonacci_iteratively(n):
    if n == 1 or n == 2:
        return 1
    a = 0
    b = 1
    c = 1
    for i in range(1, n,1):
        a = b
        b = c
        c = a+b
    return b

print(fibonacci_iteratively(8))
print(fibonacci_iteratively(2))
print(fibonacci_iteratively(3))
print(fibonacci_iteratively(11))
