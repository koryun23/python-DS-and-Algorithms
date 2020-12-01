calculations = 0
def slow_fib(n):
    global calculations
    calculations += 1
    if n < 2:
        return n
    return slow_fib(n-2)+slow_fib(n-1)

print('slow:', slow_fib(11))
print('WITHOUT DP:',calculations, 'calculations')
cache = dict()
calculations = 0
def faster_fib(n):
    global calculations
    calculations += 1
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        cache[n] = faster_fib(n-1) + faster_fib(n-2)
        return cache[n]
print('fast:',faster_fib(109))
print('WITH DP:',calculations, 'calculations')



