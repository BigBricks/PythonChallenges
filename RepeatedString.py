def repeatedString(s, n):
    countA = s.count('a')
    amountOfRepeats = n // len(s)
    total = countA * amountOfRepeats
    remainder = n % len(s)
    if remainder > 0:
        s = s[0:remainder]
        total += s.count('a')
    return total