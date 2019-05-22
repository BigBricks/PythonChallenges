def even_numbers(arr,n):
    ans = [x for x in arr if x % 2 == 0 ] 
    return ans[len(ans) - n:]