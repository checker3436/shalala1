def gam(x, eps = 10**(-8)):
    n = 1
    pr = 0
    bud = 1
    while bud - pr > eps:
        pr = bud
        bud = pr * (((1 + (1/n))**x) / (1 + (x/n)))
        n = n + 1
    return pr/x
#левый комент просто чтобы был

print(gam(3), gam(3, 0.01), gam(x = 5, eps = 10**(-10)))
