# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 8:56:38 2022

@author: carlo
"""

import numpy as np

x = np.array([[2, 5], [0, 9]])
y = np.array([[-2, -2], [-8, 6]])
z = np.array([[3, 4], [-2, 11]])


def my_kronn(x, y):
    """
    Se espera que x e y sean objetos tipo np.array
    """

    res = []
    m = x.shape[0]*y.shape[0]
    n = x.shape[1]*y.shape[1]
    for j in range(m):
        this_row = []
        for i in range(n):
            a_x = i // y.shape[1]
            b_x = i % y.shape[1]
            a_y = j // y.shape[0]
            b_y = j % y.shape[0]
            ey = x[a_y, a_x]*y[b_y, b_x]
            this_row.append(ey)
        res.append(this_row)
    print(res)
    return np.array(res)


print("Matriz inicial X")
print(x)
print("Matriz inicial Y")
print(y)
print("Matriz inicial Z")
print(z)

print()
print()

print("Propiedad distributiva por la izquierda")
print("X (x) (Y + Z)")
res = np.kron(x, (y + z))
print(res)
print()
print("X (x) Y + X (x) Z")
res = np.kron(x, y) + np.kron(x, z)
print(res)
print()
print("X (x) (Y + Z) = X (x) Y + X (x) Z")
print()
print()

print("Propiedad distributiva por la derecha")
print("(X + Y) (x) Z")
res = np.kron(x+y, z)
print(res)
print()
print("X (x) Z + Y (x) Z")
res = np.kron(x, z) + np.kron(y, z)
print(res)
print()
print("(X + Y) (x) Z = X (x) Z + Y (x) Z")
print()
print()

print("Propiedad (k * X) (x) Y = X (x) (k * Y) = k * (X (x) Y)")
print(" k = 5")
print("(k * X) (x) Y")
res = np.kron(5*x, y)
print(res)
print()
print("X (x) (k * Y)")
res = np.kron(x, 5*y)
print(res)
print()
print("k * (X (x) Y)")
res = 5*np.kron(x, y)
print(res)
print()
print("(k * X) (x) Y = X (x) (k * Y) = k * (X (x) Y)")
print()
print()

print("Propiedad asociativa")
print("(X (x) Y) (x) Z")
res = np.kron(x, y)
res = np.kron(res, z)
print(res)
print()
print("X (x) (Y (x) Z)")
res = np.kron(y, z)
res = np.kron(x, res)
print(res)
print()
print("(X (x) Y) (x) Z = X (x) (Y (x) Z)")
print()
print()
