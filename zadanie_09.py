import os
import csv

print("Текущая папка:", os.getcwd())
print("Файлы до:", os.listdir('.'))
print()

# ===== 9.2 Создание файла =====
with open('my_data.txt', 'w', encoding='utf-8') as f:
    f.write('Строка 1\n')
    f.write('Строка 2\n')
    f.write('Строка 3\n')
print("✅ my_data.txt создан\n")

# ===== 9.3 Чтение файла =====
print("--- Содержимое my_data.txt ---")
with open('my_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
print()

# ===== 9.5 CSV =====
with open('students.csv', 'w', encoding='utf-8') as f:
    f.write('name,age,city\n')
    f.write('Иван,20,Москва\n')
    f.write('Мария,22,Санкт-Петербург\n')
    f.write('Олег,19,Казань\n')
    f.write('Анна,21,Новосибирск\n')

print("--- students.csv (через csv.DictReader) ---")
with open('students.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row)
print()

print("Файлы после:", os.listdir('.'))