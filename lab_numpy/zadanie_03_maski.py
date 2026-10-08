"""Задание 3. Булевы маски и np.where()."""

import numpy as np

np.random.seed(42)

# Массив из 20 случайных чисел от 1 до 100
arr = np.random.randint(1, 101, size=20)
print("Массив:", arr)

# 1. Маска: элементы > 50
mask = arr > 50
print("\nМаска (> 50)  :", mask)
print("Элементы > 50 :", arr[mask])

# 2. Элементы в диапазоне 25..75
in_range = arr[(arr >= 25) & (arr <= 75)]
print("Диапазон 25–75:", in_range)

# 3. Заменяем элементы < 30 на 0 через np.where()
arr2 = np.where(arr < 30, 0, arr)
print("\nПосле замены < 30 на 0:", arr2)

# 4. Индексы элементов, равных максимуму
max_val = arr.max()
idx_max = np.where(arr == max_val)
print(f"\nМаксимум = {max_val}, индексы: {idx_max[0]}")

# 5. Новый массив: элементы > среднего остаются, остальные → среднее
mean_val = arr.mean()
arr3 = np.where(arr > mean_val, arr, mean_val)
print(f"\nСреднее = {mean_val:.2f}")
print("Новый массив (< среднего → среднее):", np.round(arr3, 2))
