import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol


def get_x_vect():
    x_vect = []
    x0 = -1.0
    x = x0
    while x <= 1:
        x_vect.append(x)
        x += 1.0 / 32
    x_vect = np.array(x_vect)
    return x_vect


def fun(xi):
    return 1 / (1 + 5 * pow(xi, 2))


def interpolation(x_given, fx_given, x):
    n = len(x_given)-1
    lagrpoly = np.array([lagrange(x, i, x_given) for i in range(n+1)])
    return np.dot(fx_given, lagrpoly)


def lagrange(x, i, x_given):
    n = len(x_given)-1
    y = 1.0
    for j in range(n+1):
        if i != j:
            y *= (x - x_given[j]) / (x_given[i] - x_given[j])
    return y


if __name__ == '__main__':
    X = get_x_vect()
    Y = []
    for x in X:
        y = fun(x)
        Y.append(y)
        print(x, y)
    Y = np.array(Y)
    x = np.linspace(X[0], X[len(X)-1], 130)

    y_interpolated = interpolation(X, Y, x)

    plt.title("Wykresy wielomianów rzeczywistego i interpolacyjnego Lagrange'a")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter(X, Y, color="g")
    plt.plot(x, y_interpolated, color="r")
    plt.grid()
    plt.show()

    # sym_x = Symbol('x')
    # print(interpolation(X, Y, sym_x))
