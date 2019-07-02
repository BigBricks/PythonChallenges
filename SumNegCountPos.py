def count_positives_sum_negatives(arr):
    #your code here
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        else:
            neg += x
    if arr == []:
        return []
    return [pos, neg]