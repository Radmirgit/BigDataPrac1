"""Задание 6. Изменение формы и транспонирование."""

import numpy as np

# Базовый массив из 12 чисел
arr = np.arange(12)
print("Исходный массив:", arr)

# 1. reshape 3×4
m34 = arr.reshape(3, 4)
print("\nМатрица 3×4:\n", m34)

# 2. reshape 2×6
m26 = arr.reshape(2, 6)
print("\nМатрица 2×6:\n", m26)

# 3. Вектор-столбец (12, 1)
col = arr.reshape(-1, 1)
print("\nВектор-столбец shape:", col.shape, "\n", col.T)  # .T для компактного вывода

# 4. Вектор-строка (1, 12)
row = arr.reshape(1, -1)
print("Вектор-строка shape:", row.shape, "\n", row)

print("\n" + "=" * 50)
print("ТРАНСПОНИРОВАНИЕ")
print("=" * 50)

mat = np.arange(6).reshape(2, 3)
print("\nМатрица 2×3:\n", mat, "  shape:", mat.shape)
print("Транспонированная 3×2:\n", mat.T, "  shape:", mat.T.shape)

print("\n" + "=" * 50)
print("ravel() vs flatten()")
print("=" * 50)

m = np.arange(12).reshape(3, 4)
print("\nМатрица 3×4:\n", m)

r = m.ravel()
f = m.flatten()
print("\nravel() :", r)
print("flatten():", f)

# Разница: ravel возвращает вид (view), flatten — копию
r[0] = 999
print("\nПосле изменения ravel()[0] = 999:")
print("Матрица изменилась?", m[0, 0] == 999, "← ravel — это вид (view) исходного массива")
f[1] = 888
print("После изменения flatten()[1] = 888, матрица[0,1] =", m[0, 1], "← flatten — это копия")
