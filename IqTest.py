def iq_test(numbers):
    numbers = numbers.split(" ")
    even = [w for w in range(len(numbers)) if int(numbers[w]) % 2 == 0]
    odd = [w for w in range(len(numbers)) if int(numbers[w]) % 2 != 0]
    return odd[0] + 1 if len(odd) < len(even) else even[0] + 1