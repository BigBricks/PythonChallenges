def digital_root(n):
    # ...
    if n < 10:
        return n
    acc = n % 10
    n = n - acc
    n = n / 10
    n = n + acc
    return digital_root(n)
