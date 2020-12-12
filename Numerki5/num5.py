import numpy as np


def create_a(n):
    matrix_a = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_a[i][j] = 4
            elif (i - j) == 1 or (j - i) == 1 or (j - i) == 4 or (i - j) == 4:
                matrix_a[i][j] = 1
            else:
                matrix_a[i][j] = 0
    return matrix_a


def gauss_seidel(matrix_a, vector_x, vector_b, iterations):
    n = len(matrix_a)
    for k in range(iterations):
        for i in range(n):
            temp = vector_b[i]
            for j in range(n):
                if i != j and matrix_a[i][j] != 0:
                    temp -= matrix_a[i][j] * vector_x[j]
            vector_x[i] = temp / matrix_a[i][i]
    return vector_x


def sherman_morrison(matrix_a, martix_u, matrix_v, vector_b):
    vector_u = np.array(martix_u[:, :1])
    vector_vt = np.array(matrix_v.T[0])
    vector_z = gauss_seidel(np.copy(matrix_a), np.zeros(len(vector_vt)), np.copy(vector_b), 42)
    vector_q = gauss_seidel(np.copy(matrix_a), np.zeros(len(vector_vt)), np.copy(vector_u.T[0]), 42)
    return vector_z - vector_q * (np.dot(vector_vt, vector_z) / (1 + np.dot(vector_vt, vector_q)))


if __name__ == '__main__':
    # Ax = e
    e = np.ones(64)
    A = create_a(64)
    u = np.zeros((64, 64))
    u[:, 0] = 1
    v = np.copy(u)

    print(sherman_morrison(A, u, v, e))

    A = np.array(A+(u@v.T))
    print(np.linalg.solve(A, e))

