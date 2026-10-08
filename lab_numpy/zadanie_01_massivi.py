"""Задание 1. Создание массивов и их свойства."""

import numpy as np

print("=" * 50)
print("Версия NumPy:", np.__version__)
print("=" * 50)


def info(name, arr):
    """Выводит основные свойства массива."""
    print(f"\n--- {name} ---")
    print("Массив:\n", arr)
    print("shape :", arr.shape,  " — размер по каждому измерению")
    print("dtype :", arr.dtype,  " — тип данных элементов")
    print("ndim  :", arr.ndim,   " — количество измерений")
    print("size  :", arr.size,   " — общее количество элементов")


# 1. Одномерный массив от 1 до 10
arr1 = np.arange(1, 11)
info("np.arange(1, 11)", arr1)

# 2. Матрица 3×4 из нулей
arr2 = np.zeros((3, 4))
info("np.zeros((3, 4))", arr2)

# 3. Матрица 2×5, заполненная числом 7
arr3 = np.full((2, 5), 7)
info("np.full((2, 5), 7)", arr3)

# 4. 100 равномерных точек от 0 до 1
arr4 = np.linspace(0, 1, 100)
info("np.linspace(0, 1, 100)", arr4)

# 5. Единичная матрица 5×5
arr5 = np.eye(5)
info("np.eye(5)", arr5)

# 6. 10 случайных чисел от 0 до 1 (seed=42 для воспроизводимости)
np.random.seed(42)
arr6 = np.random.rand(10)
info("np.random.rand(10) seed=42", arr6)
