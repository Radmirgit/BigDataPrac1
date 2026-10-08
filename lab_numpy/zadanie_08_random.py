"""Задание 8. Генерация случайных чисел."""

import numpy as np

print("=" * 50)
print("1. seed(42) — воспроизводимость")
print("=" * 50)

np.random.seed(42)
r1 = np.random.rand(10)
np.random.seed(42)
r2 = np.random.rand(10)
print("Запуск 1:", np.round(r1, 4))
print("Запуск 2:", np.round(r2, 4))
print("Результаты совпадают:", np.array_equal(r1, r2))

print("\n" + "=" * 50)
print("2. Равномерное распределение [-5, 5]")
print("=" * 50)

uniform = np.random.uniform(-5, 5, 1000)
print(f"mean = {uniform.mean():.4f}  (теория: 0)")
print(f"std  = {uniform.std():.4f}  (теория: ≈ 2.89)")

print("\n" + "=" * 50)
print("3. Нормальное распределение N(50, 10)")
print("=" * 50)

normal = np.random.normal(loc=50, scale=10, size=1000)
print(f"mean = {normal.mean():.4f}  (теория: 50)")
print(f"std  = {normal.std():.4f}  (теория: 10)")

print("\n" + "=" * 50)
print("4. shuffle и choice")
print("=" * 50)

arr = np.arange(1, 11)
print("До shuffle:", arr)
np.random.shuffle(arr)
print("После shuffle:", arr)

chosen = np.random.choice(arr, size=3, replace=False)
print("3 случайных элемента (без повторений):", chosen)

print("\n" + "=" * 50)
print("5. Моделирование 1000 бросков монеты (P(орёл)=0.75)")
print("=" * 50)

# 1 = орёл, 0 = решка
tosses = np.random.choice([1, 0], size=1000, p=[0.75, 0.25])
eagles = tosses.sum()
tails = 1000 - eagles
print(f"Орлов : {eagles} ({eagles/10:.1f}%)")
print(f"Решек : {tails} ({tails/10:.1f}%)")
