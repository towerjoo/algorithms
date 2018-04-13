from solution import answer


points = list(range(1, 200)) + [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10, 143]
#points = range(1, 10**6+1)
for p in points:
    print "answer for {} is: {}".format(p, answer(p))
    #if answer(p) != answer2(p):
    #    print "doesn't equal for {}".format(p)
