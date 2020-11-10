import numpy as np


def gauss_elimination(matrix_a, vector_b):
    n = len(vector_b)
    vector_z = np.zeros(n)

    # macierz trójkątna górna
    for i in range(0, n):
        for j in range(i+1, n):
            c = matrix_a[j][i] / matrix_a[i][i]
            vector_b[j] = vector_b[j] - c * vector_b[i]
            for k in range(i, n):
                if k == i:
                    matrix_a[j][k] = 0
                else:
                    matrix_a[j][k] = matrix_a[j][k] - c * matrix_a[i][k]

    # otrzymywanie wartości wektora x
    for i in range(n-1, -1, -1):
        local_sum = 0.0
        for j in range(i+1, n):
            if i != j:
                local_sum += matrix_a[i][j] * vector_z[j]
        vector_z[i] = (vector_b[i] - local_sum) / matrix_a[i][i]

    return vector_z


if __name__ == '__main__':
    A = np.array([[-116.66654, 583.33346, -333.33308, 100.00012, 100.00012],
                  [583.33346, -116.66654, -333.33308, 100.00012, 100.00012],
                  [-333.33308, -333.33308, 133.33383, 200.00025, 200.00025],
                  [100.00012, 100.00012, 200.00025, 50.000125, -649.99988],
                  [100.00012, 100.00012, 200.00025, -649.99988, 50.000125]])

    b = np.array([[-0.33388066, 1.08033290, -0.98559856, 1.31947922, -0.09473435],
                  [-0.33388066, 1.0803329, -0.98559855, 1.32655028, -0.10180541],
                  [0.72677951, 0.72677951, -0.27849178, 0.96592583, 0.96592583],
                  [0.73031505, 0.73031505, -0.27142071, 0.96946136, 0.96946136]])

    z = np.array([gauss_elimination(A, b[0]),
                  gauss_elimination(A, b[1]),
                  gauss_elimination(A, b[2]),
                  gauss_elimination(A, b[3])])

    norm1 = np.linalg.norm(b[0]-b[1])
    norm2 = np.linalg.norm(b[2]-b[3])
    norm3 = np.linalg.norm(z[0]-z[1]) / np.linalg.norm(b[0]-b[1])
    norm4 = np.linalg.norm(z[2]-z[3]) / np.linalg.norm(b[2]-b[3])

    print("z1: ", z[0], "\n")
    print("z2: ", z[1], "\n")
    print("z3: ", z[2], "\n")
    print("z4: ", z[3], "\n")

    print("||b1 - b2|| = ", norm1, "\n")
    print("||b3 - b4|| = ", norm2, "\n")
    print("||z1 - z2|| / ||b1 - b2|| = ", norm3, "\n")
    print("||z3 - z4|| / ||b3 - b4|| = ", norm4, "\n")


