def rgb(r, g, b):
    #your code here :)
    if(r < 0):
        r = 0
    if(g < 0):
        g = 0
    if(b < 0):
        b = 0
    if(r > 255):
        r = 255
    if(g > 255):
        g = 255
    if(b > 255):
        b = 255
    r1 = hex(r)[2:].upper()
    g1 = hex(g)[2:].upper()
    b1 = hex(b)[2:].upper()
    if len(r1) < 2:
        r1 = "0" + r1
    if len(g1) < 2:
        g1 = "0" + g1
    if len(b1) < 2:
        b1 = "0" + b1
    return r1 + g1 + b1