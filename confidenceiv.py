import numpy as np

def initialmv(data):
    return np.mean(data), np.var(data)

def calcurmv(xj, sj, xc, j):
    xj1 = xj + ((xc - xj) / (j + 1))
    sj1 = (((1 - (1 / j)) * (sj ** 2)) + (j + 1) * ((xj1 - xj) ** 2)) ** 0.5
    return xj1, sj1

def checkstop(s, k, l, x):
    #Checks if we have achieved 99% confidence interval with a range l or less
    za = 2.975
    print("The current l is: ", ((2 * za * s / (k) ** 0.5)/x))
    if (2 * za * s / (k) ** 0.5) < l:
        return False
    else:
        return True