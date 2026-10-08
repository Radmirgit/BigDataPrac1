"""Задание 4. Векторные операции и broadcasting."""

import numpy as np

np.random.seed(42)

# Два массива из 10 случайных чисел от 1 до 10
a = np.random.randint(1, 11, size=10).astype(float)
b = np.random.randint(1, 11, size=10).astype(float)
print("a:", a)
print("b:", b)

# 1. Поэлементные операции
print("\na + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", np.round(a / b, 2))

# 2. Скалярное произведение
print("\nСкалярное произведение np.dot(a, b):", np.dot(a, b))

# 3. Степени
print("\na в квадрате:", a ** 2)
print("a в кубе    :", a ** 3)

print("\n" + "=" * 50)
print("BROADCASTING")
print("=" * 50)

# Матрица 3×3 + вектор длиной 3 (по строкам)
mat = np.random.randint(1, 10, size=(3, 3)).astype(float)
vec_row = np.array([10.0, 20.0, 30.0])
print("\nМатрица 3×3:\n", mat)
print("Вектор-строка:", vec_row)
print("Матрица + вектор-строка (broadcasting по строкам):\n", mat + vec_row)

# Вектор-столбец (3, 1) + матрица (broadcasting по столбцам)
vec_col = np.array([[100.0], [200.0], [300.0]])
print("\nВектор-столбец (3,1):\n", vec_col)
print("Матрица + вектор-столбец (broadcasting по столбцам):\n", mat + vec_col)

# Умножение матрицы на скаляр
print("\nМатрица * 2:\n", mat * 2)

print("""
--- Что такое broadcasting ---
Broadcasting — это механизм NumPy, позволяющий выполнять операции
над массивами разных форм без явного копирования данных.
NumPy «растягивает» меньший массив до формы большего.
Пример: массив (3, 3) + массив (3,) → NumPy применяет вектор к каждой строке.
""")
