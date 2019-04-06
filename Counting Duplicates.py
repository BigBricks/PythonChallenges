from collections import Counter


def duplicate_count(text):
    # Your code goes here
    count = 0
    c = text.lower()
    j = Counter(c)
    for l in j:
        if j[l] > 1:
            count += 1
    return count

