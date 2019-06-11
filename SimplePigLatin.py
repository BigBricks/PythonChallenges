def pig_it(text):
    #your code here
    alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    j = text.split()
    for x in range(len(j)):
        if j[x] in alphabet and len(j[x]) == 1:
            j[x] = j[x].replace(j[x], j[x] + "ay")
        elif len(j[x]) > 1:
            j[x] = j[x].replace(j[x], j[x][1:] + j[x][0] + "ay")
    return " ".join(j)