"""Задание 3. Условные операторы."""

number = int(input("Введите число для проверки чётности: "))
print("Число чётное" if number % 2 == 0 else "Число нечётное")
number = int(input("Введите число для проверки кратности: "))
if number % 20 == 0:
    print("Число кратно 20")
elif number % 4 == 0:
    print("Число кратно 4")
elif number % 5 == 0:
    print("Число кратно 5")
else:
    print("Число не кратно 4 или 5")

age = int(input("Введите возраст: "))
if age < 18:
    print("Вы несовершеннолетний")
elif age <= 65:
    print("Вы взрослый")
else:
    print("Вы пенсионер")

left = float(input("Первое число: "))
operator = input("Оператор (+, -, *, /): ")
right = float(input("Второе число: "))
if operator == "+":
    result = left + right
elif operator == "-":
    result = left - right
elif operator == "*":
    result = left * right
elif operator == "/" and right != 0:
    result = left / right
else:
    result = None
    print("Ошибка: неверный оператор или деление на ноль.")
if result is not None:
    print("Результат:", result)
