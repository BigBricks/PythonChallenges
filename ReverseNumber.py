def reverse_number(n):
    if(n == abs(n)):
        return int("".join(reversed(str(n))))
    else:
        n = abs(n)
        return int("-"+"".join(reversed(str(n))))