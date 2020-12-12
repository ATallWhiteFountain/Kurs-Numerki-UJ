# import numpy as np
# import matplotlib.pyplot as plt
#
#
# #  Znajduje współczynniki wielomianu interpolacyjnego
#
# x_s = [0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500]
# fx_s = [0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307]
# n = len(x_s)
#
# matrix_X = np.zeros((n, n))
# for i in range(n):
#     for j in range(n):
#         k = n-1-j
#         matrix_X[i][j] = x_s[i]**k
# vector_f = np.array(fx_s)
#
# vector_a = np.array(np.linalg.solve(matrix_X, vector_f))
# results = np.round(vector_a[::-1], 4)
# print(results)
#
#
# # Sporządzam wykres
#
# def fun(x, coefs):
#     n = len(coefs)
#     retval = 0
#     for i in range(n):
#         k = n - 1 - i
#         retval += coefs[i] * (x**k)
#     return retval
#
#
# interval = np.linspace(-1, 1, 600)
#
# plt.figure(figsize=(12, 8))
#
# plt.plot(interval, fun(interval, vector_a), label="interpolation function")
# plt.scatter(x_s, fx_s, label="interpolation points", color="C3")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("f(x)")
#
# plt.show()
#
#
import numpy as np
import matplotlib.pyplot as plt


#  Znajduje współczynniki wielomianu interpolacyjnego

def lagrange(n):
    coefs = np.zeros(n)
    for k in range(n):
        for j in range(n):
            coefs[k] = np.sum()
    return coefs


x_s = np.array([0.062500, 0.187500, 0.312500, 0.437500, 0.562500, 0.687500, 0.812500, 0.937500])
fx_s = np.array([0.687959, 0.073443, -0.517558, -1.077264, -1.600455, -2.080815, -2.507266, -2.860307])
n = len(x_s)

matrix_X = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        k = n-1-j
        matrix_X[i][j] = x_s[i]**k
vector_f = np.array(fx_s)

vector_a = np.array(np.linalg.solve(matrix_X, vector_f))
results = np.round(vector_a[::-1], 4)
print(results)


# Sporządzam wykres

def fun(x, coefs):
    n = len(coefs)
    retval = 0
    for i in range(n):
        k = n - 1 - i
        retval += coefs[i] * (x**k)
    return retval


interval = np.linspace(-1, 1, 600)

plt.figure(figsize=(12, 8))

plt.plot(interval, fun(interval, vector_a), label="interpolation function")
plt.scatter(x_s, fx_s, label="interpolation points", color="C3")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()




