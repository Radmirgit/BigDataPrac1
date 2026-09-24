#Задание 10. Итоговое практическое задание 

import os
import random
import statistics

# 1. Запрашиваем имя файла у пользователя
filename = input("Введите имя файла (например, numbers.txt): ").strip()
if not filename:
    filename = "numbers.txt"

# 2. Генерируем 100 случайных чисел от 0 до 100 и записываем в файл
numbers_generated = [random.randint(0, 100) for _ in range(100)]

with open(filename, 'w', encoding='utf-8') as f:
    for num in numbers_generated:
        f.write(f"{num}\n")

print(f"✅ Файл '{filename}' создан. Записано {len(numbers_generated)} чисел.")

# 3. Считываем числа из файла в список
with open(filename, 'r', encoding='utf-8') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

# 4. Вычисляем статистику
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)
median = statistics.median(numbers)
evens = sum(1 for n in numbers if n % 2 == 0)
odds = sum(1 for n in numbers if n % 2 != 0)

# Выводим на экран
print(f"\nМинимальное:  {minimum}")
print(f"Максимальное: {maximum}")
print(f"Среднее:      {mean:.2f}")
print(f"Медиана:      {median}")
print(f"Чётных:       {evens}")
print(f"Нечётных:     {odds}")

# 5. Сохраняем результаты в results.txt
results_text = (
    f"Минимум: {minimum}\n"
    f"Максимум: {maximum}\n"
    f"Среднее: {mean:.2f}\n"
    f"Медиана: {median}\n"
    f"Чётных: {evens}\n"
    f"Нечётных: {odds}\n"
)

output_filename = "results.txt"
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(results_text)

# 6. Сообщаем о завершении и показываем, где лежит файл на диске
full_path = os.path.abspath(output_filename)
print(f"\n✅ Результаты успешно сохранены в файл: {output_filename}")
print(f"📁 Полный путь: {full_path}")