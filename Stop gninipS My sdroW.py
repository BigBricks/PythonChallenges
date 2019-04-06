def spin_words(sentence):
    # Your code goes here
    if len(sentence) == 0:
        return None
    s = sentence.split()
    arr = []
    for x in s:
        if len(x) > 4:
            arr.append(reverse(x))
        else:
            arr.append(x)
    return " ".join(arr)


def reverse(word):
    str = ""
    for s in word:
        str = s + str
    return str
