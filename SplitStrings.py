def solution(s):
    arr = []
    if len(s) == 0: return []
    elif len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            arr.append(s[i:i+2])
        return arr
    else: 
        for i in range(0, len(s) - 1, 2):
            arr.append(s[i:i+2])
        arr.append(s[-1] + "_")
        return arr