import math

def greet(name):
    print(f"Привет, {name}!")

# Вызовы с разными именами
greet("Иван")
greet("Мария")
greet("Алексей")

def is_prime(n):
    if n < 2:                      # 0 и 1 не простые
        return False
    if n == 2:                     # 2 — простое
        return True
    if n % 2 == 0:                 # чётные > 2 не простые
        return False
    # проверяем только нечётные делители до √n
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Проверка
for x in [1, 2, 3, 4, 5, 9, 11, 15, 17, 25, 29, 97]:
    print(f"{x}: {is_prime(x)}")

# Итеративный способ (цикл)
def factorial_iter(n):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Рекурсивный способ
def factorial_rec(n):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n in (0, 1):                # база рекурсии
        return 1
    return n * factorial_rec(n - 1)

# Проверка
for n in range(0, 8):
    print(f"{n}! = iter: {factorial_iter(n)}, rec: {factorial_rec(n)}")

print("\n10! =", factorial_iter(10), "\n")

def average(numbers):
    if not numbers:                # пустой список
        return 0
    return sum(numbers) / len(numbers)

print(average([1, 2, 3, 4, 5]))   # 3.0
print(average([10, 20]))          # 15.0
print(average([]), "\n")                # 0

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all(10))                # 10
print(sum_all())                  # 0
print(sum_all(1, 2, 3), "\n")           # 6

def min_max(lst):
    return min(lst), max(lst)
mn, mx = min_max([10, 20, 5, 30])
print(mn, mx)
