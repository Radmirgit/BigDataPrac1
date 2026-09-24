"""Задание 4. Циклы."""

print("Числа 1–10:", *range(1, 11))
for i in range(1, 11):
    print(f"{i}² = {i ** 2}")
print("Чётные 2–20:", *range(2, 21, 2))

n = 10
while n:
    print(n, end=" ")
    n -= 1
print()
while True:
    value = int(input("Введите число (0 — выход): "))
    if value == 0:
        break
    print("Вы ввели:", value)

limit = int(input("Введите N: "))
print(f"Сумма от 1 до {limit}:", sum(range(1, limit + 1)))
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
    
