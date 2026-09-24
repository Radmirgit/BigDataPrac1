import math
import random
import string

print("sin(π/2) =", math.sin(math.pi / 2))
print("cos(0)   =", math.cos(0))
print("log(100) =", math.log(100))        # натуральный логарифм
print("log10(100) =", math.log10(100))    # десятичный (для сравнения)
print("sqrt(256) =", math.sqrt(256))
print("factorial(5) =", math.factorial(5))

# 1. Случайное число от 0 до 1 (float)
r = random.random()
print("random.random():", r)

# 2. Случайное целое от 1 до 100 (включительно)
n = random.randint(1, 100)
print("random.randint(1, 100):", n)

# 3. Случайный элемент из списка
fruits = ["яблоко", "банан", "вишня", "груша", "слива"]
pick = random.choice(fruits)
print("random.choice:", pick)

# 4. Перемешивание списка 
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(cards)
print("После shuffle:", cards)

print("Без seed:", [random.randint(1, 10) for _ in range(5)])

# Задаём seed
random.seed(42)
print("seed=42 (1-й запуск):", [random.randint(1, 10) for _ in range(5)])

# Другой seed — другая последовательность
random.seed(1)
print("seed=1:", [random.randint(1, 10) for _ in range(5)])

def generate_password(length):
    """Генерирует случайный пароль из букв и цифр заданной длины."""
    if length <= 0:
        raise ValueError("Длина пароля должна быть положительной")

    # Набор символов: прописные + строчные буквы + цифры
    chars = string.ascii_letters + string.digits
    # ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits        = '0123456789'

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# Проверяем
print(generate_password(8))
print(generate_password(12))
print(generate_password(16))
print(generate_password(4))