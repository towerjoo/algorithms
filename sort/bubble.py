def bubble_sort(arr):
    # O(n^2)
    s = len(arr)
    i = s - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i] # swap
            j -= 1
        i -= 1
    return arr
