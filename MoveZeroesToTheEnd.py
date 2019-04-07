def move_zeros(array):
    #your code here
    arr = []
    zero = []
    for x in array:
        if x == 0 and x is not False:
            zero.append(x)
        else:
            arr.append(x)
    
    return arr + zero