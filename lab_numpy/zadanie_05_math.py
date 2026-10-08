"""Задание 5. Математические функции."""

import numpy as np

# 1. Массив из 100 точек от -2π до 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
print("Диапазон x: от", round(x[0], 4), "до", round(x[-1], 4))

# 2. sin, cos, tan
sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)
print("\nПервые 5 значений sin(x):", np.round(sin_x[:5], 4))
print("Первые 5 значений cos(x):", np.round(cos_x[:5], 4))

# 3. exp(x) для 0..5, проверяем exp(0) = 1
x_exp = np.linspace(0, 5, 6)
print("\nexp(x) для x =", x_exp, ":", np.round(np.exp(x_exp), 4))
print("exp(0) =", np.exp(0), " → должно быть 1.0")

# 4. log для [1, 10, 100, 1000]
vals = np.array([1, 10, 100, 1000])
print("\nlog(x) для", vals, ":", np.round(np.log(vals), 4))
print("log(1) =", np.log(1), " → должно быть 0.0")

# 5. sqrt для [1, 4, 9, 16, 25]
sq = np.array([1, 4, 9, 16, 25])
print("\nsqrt:", sq, "→", np.sqrt(sq))

# 6. Перевод 90° в радианы
rad = np.radians(90)
print(f"\n90° в радианах = {rad:.6f}, π/2 = {np.pi / 2:.6f}")
print("Разница:", abs(rad - np.pi / 2))

# 7. np.abs() для массива с отрицательными значениями
neg = np.array([-5, -3, -1, 0, 2, 4, -7])
print("\nМассив:", neg)
print("np.abs():", np.abs(neg))
