"""
1. we have two arrays(one is the original unordered one, and the other is an empty array, i.e ordered array)
2. each time select the smallest element from the unordered array, and append it to the ordered array
3. continue, until unordered one is empty

"""

def select_sort(arr):
    # O(n^2)
    ordered = []
    while True:
        n = len(arr)
        if n == 0:
            break
        smallest_index = 0
        for i in range(1, n):
            if arr[smallest_index] > arr[i]:
                smallest_index = i
        ordered.append(arr.pop(smallest_index))
    return ordered
