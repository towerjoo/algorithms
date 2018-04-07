"""
this can be a recursive process, i.e

1. split an array into two arrays
2. go to 1, until the split array has only 1 element and return that single element array
3. merge the two ordered arrays into one array by comparing
"""
def merge(a, b):
    out = []
    i = j = 0
    sa = len(a)
    sb = len(b)
    while True:
        if i >= sa:
            # move the remaining
            out.extend(b[j:])
            break
        if j >= sb:
            # move the remaining
            out.extend(a[i:])
            break
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out

def merge_sort(arr):
    # O(nlogn)
    s = len(arr)
    if s == 1:
        return arr
    mid = s / 2
    a = merge_sort(arr[:mid])
    b = merge_sort(arr[mid:])
    return merge(a, b)
