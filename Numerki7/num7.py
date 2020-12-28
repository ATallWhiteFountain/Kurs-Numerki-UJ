import numpy as np
import math
from scipy import integrate


def fun(x):
    return np.sin(math.pi * ((1 + math.sqrt(x)) / (1 + pow(x, 2)))) * math.exp(-x)


def trapeze_method(f, a, b, n):
    h = (b-a)/n
    x = a
    fx = f(x)
    for i in range(1, n):
        x += h
        fx += 2*f(x)
    return (fx + f(b)) * h * 0.5


def romberg(f, a, b, eps, nmax):
    Q = np.zeros((nmax, nmax), float)
    for i in range(0, nmax):
        n = 2**i
        Q[i, 0] = trapeze_method(f, a, b, n)
        for k in range(0, i):
            Q[i, k+1] = (4**(k+1) * Q[i, k] - Q[i-1, k]) / (4**(k+1)-1)
            if i > 0 and abs(Q[i, k+1] - Q[i, k]) < eps:
                break
        print(Q[i, 0:i+1])
    return Q


def fun2(x):
    return math.exp(-x)


if __name__ == '__main__':
    a = 0.0
    b = 17.0
    c = np.inf
    eps = 1.0e-17
    nmax = 18

    A = romberg(fun, a, b, eps, nmax)
    I1 = A[nmax-1, nmax-1]
    err, I2 = integrate.quad(fun2, b, c)
    print(I1)
    print(I2)
    print(I1 + I2)
