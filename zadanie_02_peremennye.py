"""Задание 2. Переменные и базовые операции."""

a, b, c, d = 10, 3.14, "Hello", True
for value in (a, b, c, d):
    print(value, type(value))
print("a как строка:", str(a), type(str(a)))
print("'123' как число:", int("123"), type(int("123")))

x, y = 15, 4
print("Сложение:", x + y, "Вычитание:", x - y)
print("Умножение:", x * y, "Деление:", x / y)
print("Целочисленное деление:", x // y, "Остаток:", x % y, "Степень:", x ** y)
print(10 > 5, 10 == 10, 10 != 5, not True)
print((5 > 3) and (2 < 4), (5 > 3) or (2 > 4))

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
print(f"Привет, {name}! Через 5 лет вам будет {age + 5} лет.")
