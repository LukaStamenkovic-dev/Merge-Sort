
def sum_iterative(n):
    sum = n
    while n > 0:
        n -= 1
        sum += n
    return sum

# RECURSION ima base case koji je najedstavnije resenje kada ne moramo nsita da radimo i recursive case

def sum_recursive(n):
    if n == 1:
        return n # Base case
    else:
        return n + sum_recursive(n - 1) # Recursive case
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
    
