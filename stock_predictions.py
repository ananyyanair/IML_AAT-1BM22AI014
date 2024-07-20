import numpy as np
a = 2 / 6
exp = np.array([a * (1 - a) ** (5 - i) for i in range(1, 6)]) + (1 - a) ** 5 / 5 
def printtransactions(m, k, d, name, owned, prices):
    max_f = None
    min_f = None 
    for i in range(k):
        f = getcema(prices[i]) - np.mean(prices[i])
        if owned[i] > 0 and f > 0 and (max_f is None or f > max_f[0]):
            max_f = (f, '{0} SELL {1}'.format(name[i], owned[i]))
        elif m > prices[i][-1] and d > 0 and f > 0 and (min_f is None or f < min_f[0]):
            min_f = (f, '{0} BUY {1}'.format(name[i], int(m / prices[i][-1])))
    if max_f is not None and min_f is not None:
        print(2)
    elif max_f is not None or min_f is not None:
        print(1)
    else:
        print(0)
    if max_f is not None:
        print(max_f[1])
    if min_f is not None:
        print(min_f[1]) 
def getcema(a):
    return np.dot(exp, a)
def readandrun():
    line = input().split()
    m, k, d = float(line[0]), int(line[1]), int(line[2])
    name = []
    owned = []
    prices = []
    for i in range(k):
        line = input().split()
        name.append(line[0])
        owned.append(int(line[1]))
        prices.append(list(map(float, line[2:])))
    printtransactions(m, k, d, name, owned, prices)
readandrun()