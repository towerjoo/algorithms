import math


def answer(total_lambs):
    # generous handout is a geometric sequence(q=2), Sn
    # stingy handout is a Fib sequence
    if total_lambs in [0, 1, 2]:
        return 0
    generous_total = int(math.log(total_lambs+1, 2))

    F1 = 1
    F2 = 1
    sum_stingy = 2
    stingy_total = 2
    while True:
        F1, F2 = F2, F1+F2
        sum_stingy += F2
        if sum_stingy > total_lambs:
            break
        stingy_total += 1
    return stingy_total - generous_total
