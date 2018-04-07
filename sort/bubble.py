"""
1. get the last element of the unordered array
2. compare it to the remaining elements one by one
3. if that element is smaller, then swap the two elements
4. so that each round will bubble the biggest one to the end of the unordered array
5. go to 1 to the remaining unordered array(i.e the array excluding the bubbled element)
"""

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
