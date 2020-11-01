import numpy as np


def tridiagonal_matrix_alg(a, b, c, d):

    n = len(d)
    x = np.zeros(n, float)

    c_prim = np.zeros(n-1, float)
    d_prim = np.zeros(n, float)
    c_prim[0] = c[0]/b[0]
    d_prim[0] = d[0]/b[0]
    for i in range(1, n-1):
        c_prim[i] = c[i]/(b[i] - a[i-1]*c_prim[i-1])
    for i in range(1, n):
        d_prim[i] = (d[i] - a[i-1]*d_prim[i-1])/(b[i] - a[i-1]*c_prim[i-1])

    x[n-1] = d_prim[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = d_prim[i-1] - c_prim[i-1]*x[i]
    return x


if __name__ == '__main__':
    aa = np.array([1, 1, 1, 1, 1, 1])
    bb = np.array([4, 4, 4, 4, 4, 4, 4])
    cc = np.array([1, 1, 1, 1, 1, 1])
    dd = np.array([1, 2, 3, 4, 5, 6, 7])
    print("x elements: ")
    print(tridiagonal_matrix_alg(aa, bb, cc, dd))
