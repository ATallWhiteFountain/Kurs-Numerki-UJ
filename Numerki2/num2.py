import numpy as np


def solve_matrix(matrix_a, vector_d):

    vector_x = np.array([0, 0, 0, 0, 0, 0, 0], float)
    n = len(vector_x)

    # macierz trojkątna górna
    for i in range(0, n):
        for j in range(i+1, n):
            c = matrix_a[j][i] / matrix_a[i][i]
            vector_d[j] = vector_d[j] - c * vector_d[i]
            for k in range(i, n):
                if k == i:
                    matrix_a[j][k] = 0
                else:
                    matrix_a[j][k] = matrix_a[j][k] - c * matrix_a[i][k]

    # otrzymywanie wartości wektora x
    for i in range(n-1, -1, -1):
        local_sum = 0.0
        for j in range(i + 1, n):
            if i != j:
                local_sum += matrix_a[i][j] * vector_x[j]
        vector_x[i] = (vector_d[i] - local_sum) / matrix_a[i][i]

    return vector_x


if __name__ == '__main__':
    # Ax = b
    A = np.asarray([[4, 1, 0, 0, 0, 0, 1],
                    [1, 4, 1, 0, 0, 0, 0],
                    [0, 1, 4, 1, 0, 0, 0],
                    [0, 0, 1, 4, 1, 0, 0],
                    [0, 0, 0, 1, 4, 1, 0],
                    [0, 0, 0, 0, 1, 4, 1],
                    [0, 0, 0, 0, 0, 1, 4]], float)
    b = np.array([1, 2, 3, 4, 5, 6, 7], float)
    x = solve_matrix(A, b)
    print(x)
