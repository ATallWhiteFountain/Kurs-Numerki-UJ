import numpy as np


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


def gauss(matrix_a, vector_d):

    vector_x = np.array([0, 0, 0, 0, 0, 0, 0], float)
    n = len(vector_x)
    for i in range(0, n):
        for j in range(i+1, n):
            c = matrix_a[j][i] / matrix_a[i][i]
            vector_d[j] = vector_d[j] - c * vector_d[i]
            for k in range(i, n):
                if k == i:
                    matrix_a[j][k] = 0
                else:
                    matrix_a[j][k] = matrix_a[j][k] - c * matrix_a[i][k]
    for i in range(n-1, -1, -1):
        local_sum = 0.0
        for j in range(i + 1, n):
            if i != j:
                local_sum += matrix_a[i][j] * vector_x[j]
        vector_x[i] = (vector_d[i] - local_sum) / matrix_a[i][i]

    return vector_x


def sherman_morrison(matrix_A, martix_u, matrix_v, vector_b):
    vector_u = np.array(martix_u[:, :1])
    vector_vt = np.array(matrix_v.T[0])
    vector_z = thomas(matrix_A.diagonal(-1), matrix_A.diagonal(), matrix_A.diagonal(1), vector_b)
    vector_q = thomas(matrix_A.diagonal(-1), matrix_A.diagonal(), matrix_A.diagonal(1), vector_u)

    return vector_z - vector_q * (np.dot(vector_vt, vector_z) / (1 + np.dot(vector_vt, vector_q)))


if __name__ == '__main__':
    # policzyc x mając Ax = b
    # (1) Az = b
    # (2) Aq = u
    # (3) x = z - (v{^T} z)q / 1+{v^T} q

    b = np.array([1, 2, 3, 4, 5, 6, 7], float)

    A = np.array([[3, 1, 0, 0, 0, 0, 0],
                    [1, 4, 1, 0, 0, 0, 0],
                    [0, 1, 4, 1, 0, 0, 0],
                    [0, 0, 1, 4, 1, 0, 0],
                    [0, 0, 0, 1, 4, 1, 0],
                    [0, 0, 0, 0, 1, 4, 1],
                    [0, 0, 0, 0, 0, 1, 3]], float)
    v = np.array([[1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0]], float)
    u = np.copy(v)

    x = gauss(A+(u@v.T), b)
    print(x)
    x = sherman_morrison(A, u, v, b)
    print(x)

