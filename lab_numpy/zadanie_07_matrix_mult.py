"""Задание 7. Матричное умножение."""

import numpy as np

# Две матрицы 2×2
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("A:\n", A)
print("B:\n", B)

# 1. Поэлементное умножение
print("\nПоэлементное A * B:\n", A * B)

# 2. Матричное умножение через np.dot()
print("\nМатричное np.dot(A, B):\n", np.dot(A, B))

# 3. Матричное умножение через оператор @
print("Матричное A @ B:\n", A @ B)
print("np.dot == @:", np.array_equal(np.dot(A, B), A @ B))

print("\n" + "=" * 50)

# 4. Матрицы A(2×3) и B(3×4)
A23 = np.array([[1, 2, 3],
                [4, 5, 6]])
B34 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

result = A23 @ B34
print("\nA(2×3) @ B(3×4) = результат shape:", result.shape)
print(result)

# 5. Попытка умножить матрицы одинаковой формы (2×3) @ (2×3) — должна быть ошибка
A_wrong = np.ones((2, 3))
B_wrong = np.ones((2, 3))
print("\nПопытка A(2×3) @ B(2×3):")
try:
    A_wrong @ B_wrong
except ValueError as e:
    print("Ошибка:", e)
    print("Причина: внутренние размеры не совпадают (3 ≠ 2).")

# 6. Проверка A @ I = A
I = np.eye(2)
print("\nЕдиничная матрица I:\n", I)
print("A @ I:\n", A @ I)
print("A @ I == A:", np.array_equal(A @ I, A))
