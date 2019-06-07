from collections import Counter
def duplicate_encode(word):
    #your code here
    counter = Counter(word.lower())
    s = ""
    for x in word.lower():
        if counter[x] > 1:
            s += ")"
        else:
            s += "("
    return s