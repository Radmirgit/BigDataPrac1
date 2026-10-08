"""Задание 9. Статистика и агрегация."""

import numpy as np

np.random.seed(42)

print("=" * 50)
print("1. Статистика для N(50, 10)")
print("=" * 50)

data = np.random.normal(loc=50, scale=10, size=1000)

print(f"min    = {data.min():.4f}")
print(f"max    = {data.max():.4f}")
print(f"sum    = {data.sum():.2f}")
print(f"mean   = {data.mean():.4f}")
print(f"std    = {data.std():.4f}")
print(f"var    = {data.var():.4f}")
print(f"median = {np.median(data):.4f}")

print(f"\nИндекс минимума: {data.argmin()} (значение: {data[data.argmin()]:.4f})")
print(f"Индекс максимума: {data.argmax()} (значение: {data[data.argmax()]:.4f})")

# Правило одной сигмы (μ ± σ)
mu, sigma = data.mean(), data.std()
in_sigma = np.sum((data >= mu - sigma) & (data <= mu + sigma))
print(f"\nВ диапазоне μ ± σ ({mu:.1f} ± {sigma:.1f}): {in_sigma} значений"
      f" = {in_sigma / 10:.1f}%  (теория: 68.3%)")

# Значений > 60
above_60 = np.sum(data > 60)
print(f"Значений > 60: {above_60} ({above_60 / 10:.1f}%)")

print("\n" + "=" * 50)
print("2. Матрица 5×4: суммы и средние по осям")
print("=" * 50)

mat = np.random.randint(0, 101, size=(5, 4)).astype(float)
print("Матрица 5×4:\n", mat)
print("\nСумма всех элементов    :", mat.sum())
print("Сумма по axis=0 (по строкам):", mat.sum(axis=0))
print("Сумма по axis=1 (по столбцам):", mat.sum(axis=1))
print("Среднее по строкам :", np.round(mat.mean(axis=0), 2))
print("Среднее по столбцам:", np.round(mat.mean(axis=1), 2))

print("\n" + "=" * 50)
print("3. cumsum и cumprod для [1, 2, 3, 4, 5]")
print("=" * 50)

arr = np.array([1, 2, 3, 4, 5])
cs = np.cumsum(arr)
cp = np.cumprod(arr)
print("Массив   :", arr)
print("cumsum() :", cs,  " ← 1, 1+2=3, 3+3=6, ...")
print("cumprod():", cp, " ← 1, 1×2=2, 2×3=6, ...")
print("Первый cumsum  = arr[0]         =", cs[0])
print("Первый cumprod = arr[0]         =", cp[0])
