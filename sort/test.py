import random

from merge import merge_sort
from bubble import bubble_sort
from select import select_sort
from insert import insert_sort
    
if __name__ == "__main__":
    sort = insert_sort
    a = random.sample(range(100), 20)
    print "before sorting: ", a
    print "after sorting: ", sort(a)
