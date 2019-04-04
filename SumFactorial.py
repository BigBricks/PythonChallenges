def factorial(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial
def sum_factorial(lst):
    sum = 0
    for x in lst: 
        sum += factorial(x)
        
    return sum