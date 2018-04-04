import random

from merge import merge_sort
from bubble import bubble_sort
    
if __name__ == "__main__":
    sort = bubble_sort
    a = random.sample(range(100), 20)
    print "before sorting: ", a
    print "after sorting: ", sort(a)
