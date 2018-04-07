"""
1. we have two arrays, one is the original unordered array A, another is the ordered arary B(initially it's empty)
2. each round, we pick an element from A, and insert it to the correct position of B(ensure B's order)
3. keep the process until A is empty

"""
def insert_sort(arr):
    # O(n^2)
    ordered = []
    while True:
        n = len(arr)
        if n == 0:
            break
        e = arr.pop(0) # we can also start from the end
        i = 0
        insert_index = -1
        for i, o in enumerate(ordered):
            if e < o:
                insert_index = i
                break
        if insert_index == -1:
            insert_index = len(ordered) # insert to the end
        ordered.insert(insert_index, e)
    return ordered
                
