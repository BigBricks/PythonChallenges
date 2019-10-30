def isValidWalk(walk):
    #determine if walk is valid
    n = 0
    s = 0
    w = 0
    e = 0
    count = len(walk);
    if count != 10:
        return False
    up = ""
    side = ""
    for x in walk:
        if x == "n":
            n += 1  
        if x == "s":
            s += 1  
        if x == "e":
            e += 1  
        if x == "w":
            w += 1  
    if w > e:
        side = "w"
    elif e > w:
        side = "e"
    if n > s:
        up = "n"
    elif s > n:
        up = "s"
    if up == side:
        return True
    return False
    
        