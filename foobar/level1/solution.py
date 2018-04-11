def answer(x, y):
    longer, shorter = (x, y) if len(x) > len(y) else (y, x)
    return set(longer).difference(set(shorter)).pop()

if __name__ == "__main__":
    import random
    N = random.randint(1, 100)
    x = random.sample(range(-1000, 1001), N)
    y = x[:] # deep copy
    random.shuffle(y)
    y.insert(random.randint(0, N), random.randint(-1000, 1001))
    print x
    print y
    if random.random() > .5:
        print answer(x, y)
    else:
        print answer(y, x)
