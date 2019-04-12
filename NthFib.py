def nth_fib(n):
    return fibonacci(n - 1)


memo = {0: 0, 1: 1}


def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        for x in range(2, n + 1):
            value = fibonacci(x - 1) + fibonacci(x - 2)
            memo[x] = value
    return memo[n]
