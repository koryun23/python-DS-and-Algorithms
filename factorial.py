def factorial_recursively(number):
    if number == 1:
        return 1
    return number * factorial_recursively(number-1)


def factorial_iteritively(number):
    fact = 1
    for i in range(1, number+1,):
        fact *= i
    return fact

print(factorial_iteritively(8))
print(factorial_recursively(8))