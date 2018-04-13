from solution import answer


points = [0, 1, 2, 3, 4, 5, 100, 1000, 10000, 100000, 1000000]
for p in points:
    print "answerr for {} is: {}".format(p, answer(p))
