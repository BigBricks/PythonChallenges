def sort_array(source_array):
    # Return a sorted array.
    arr = sorted(f for f in source_array if f % 2 != 0 and f != 0)
    final = source_array
    i = 0
    for x in range(len(final)):
        if final[x] != 0 and final[x] % 2 != 0:
            final[x] = arr[i]
            i += 1
    return final
