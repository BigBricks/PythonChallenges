def divisors(integer):
    j = [x for x in range(2, integer) if integer % x == 0]
    if j == []:
        return "{0} is prime".format(integer)
    return j