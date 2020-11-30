import numpy as np


def create_a(n):
    matrix_a = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_a[i][j] = 4
            if (i - j) == 1 or (j - i) == 1 or (j - i) == 4 or (i - j) == 4:
                matrix_a[i][j] = 1
    return matrix_a


def gauss_seidel(matrix_a, vector_x, vector_b, iterations):
    n = len(matrix_a)
    for k in range(iterations):
        for i in range(n):
            temp = vector_b[i]
            for j in range(n):
                if i != j:
                    temp -= matrix_a[i][j] * vector_x[j]
            vector_x[i] = temp / matrix_a[i][i]
    return vector_x


def conjugate_gradients(matrix_a, vector_x, vector_b, iterations):
    r = vector_b - np.dot(matrix_a, vector_x)
    p = r
    rsold = np.dot(r.T, r)
    for k in range(iterations):
        Ap = np.dot(matrix_a, p)
        alpha = rsold / np.dot(np.transpose(p), Ap)
        vector_x = vector_x + np.dot(alpha, p)
        r = r - np.dot(alpha, Ap)
        rsnew = np.dot(np.transpose(r), r)
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    return vector_x


if __name__ == '__main__':
    # Ax = e
    # a) Gauss-Seidla
    # b) gradienty sprzężone

    dim = 128
    e = np.ones(dim)
    x = np.zeros(dim)
    a = create_a(dim)

    print(gauss_seidel(a, x, e, 40))
    x = np.zeros(dim)

    print("\n\n", conjugate_gradients(a, x, e, 20))
