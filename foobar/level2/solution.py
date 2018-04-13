import math

# the tricky part is: the remaining number might also fit a henchman

def answer(total_lambs):
    # generous handout is a geometric sequence(q=2), Sn
    # stingy handout is a Fib sequence
    # for geometric sequence

    generous_total = int(math.log(total_lambs+1, 2))
    last = int(2 ** (generous_total - 1))
    last2 = int(2 ** (generous_total - 2))
    left = total_lambs - (2 * last - 1)
    if left >= (last + last2):
        generous_total += 1

    # for fib sequence, sum(F(n)) = F(n+2) - 1
    phi = (math.sqrt(5) + 1) / 2
    stingy_total = int(math.log((total_lambs + 1) * math.sqrt(5) + .5, phi)) - 2

    last = int(phi ** stingy_total / math.sqrt(5) + .5)
    last2 = int(phi ** stingy_total / math.sqrt(5) + .5)
    left = total_lambs - (int(phi ** (stingy_total + 2) / math.sqrt(5) + .5) - 1)
    if left >= (last + last2):
        stingy_total += 1
    return stingy_total - generous_total
