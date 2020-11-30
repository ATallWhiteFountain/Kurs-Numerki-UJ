import numpy as np


def create_a(n):
    matrix_a = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_a[i][j] = 5
            elif (i - j) == 1 or (j - i) == 1 or (j - i) == 4 or (i - j) == 4:
                matrix_a[i][j] = 2
            else:
                matrix_a[i][j] = 1
    return matrix_a


def thomas(a, b, c, d):
    nf = len(d)
    ac, bc, cc, dc = map(np.array, (a, b, c, d))
    for it in range(1, nf):
        mc = ac[it - 1] / bc[it - 1]
        bc[it] = bc[it] - mc * cc[it - 1]
    dc[it] = dc[it] - mc * dc[it - 1]
    xc = bc
    xc[-1] = dc[-1] / bc[-1]
    for il in range(nf - 2, -1, -1):
        xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]
    return xc


def preconditioner(matrix_a):
    n = len(matrix_a[0])
    jacobi = np.zeros((n, n))
    diag = np.diagonal(matrix_a)
    for i in range(n):
        for j in range(n):
            if i == j:
                jacobi[i][j] = diag[i]
    return jacobi


def preconditioned_conjugate_gradients(matrix_a, vector_x, vector_b, iterations):
    r = vector_b - np.dot(matrix_a, vector_x)
    matrix_m = preconditioner(matrix_a)
    z = thomas(matrix_m.diagonal(-1), matrix_m.diagonal(), matrix_m.diagonal(1), r)
    p = z
    rsold = np.dot(r.T, z)
    for k in range(iterations):
        Ap = np.dot(matrix_a, p)
        alpha = float(rsold / np.dot(np.transpose(p), Ap))
        vector_x = vector_x + np.dot(alpha, p)
        r = r - np.dot(alpha, Ap)
        z = thomas(matrix_m.diagonal(-1), matrix_m.diagonal(), matrix_m.diagonal(1), r)
        rsnew = np.dot(np.transpose(r), z)
        p = z + (rsnew / rsold) * p
        rsold = rsnew
    return vector_x


if __name__ == '__main__':
    e = np.ones(64)
    x = np.zeros(64)
    A = create_a(64)
    print(np.linalg.solve(A, e))
    print(preconditioned_conjugate_gradients(A, x, e, 5))
