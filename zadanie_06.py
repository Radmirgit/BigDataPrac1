# Создаём кортеж
t = (10, 20, 30, 40)
print("Кортеж:", t)

# Доступ по индексу
print("Первый элемент:", t[0])
print("Второй элемент:", t[1])
print("Последний элемент:", t[-1])

# Срез
print("Срез [1:3]:", t[1:3])

# Попытка изменить элемент → ошибка
try:
    t[0] = 99
except TypeError as e:
    print("Ошибка:", e)

# Длина кортежа
print("Длина:", len(t), "\n")

# Создаём словарь
student = {
    'name': 'Иван',
    'age': 20,
    'city': 'Москва',
    'grades': [5, 4, 3, 5]
}
print("Словарь:", student)

# Вывод отдельных полей
print("Имя:", student['name'])
print("Возраст:", student['age'])

# Добавляем новый предмет с оценкой
student['subject'] = 'Математика'
student['subject_grade'] = 5
print("\nПосле добавления предмета:", student)

# Удаляем один ключ
del student['city']
print("\nПосле удаления 'city':", student)

# Перебор всех ключей и значений
print("\n--- Перебор словаря ---")
for key, value in student.items():
    print(f"{key} : {value}")

# Дополнительно: только ключи и только значения
print("\nКлючи:", list(student.keys()))
print("Значения:", list(student.values()), "\n")

# Создаём два множества
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A =", A)
print("B =", B)

# Объединение (все элементы из обоих)
print("\nОбъединение A | B:", A | B)
print("Через метод:", A.union(B))

# Пересечение (общие элементы)
print("\nПересечение A & B:", A & B)
print("Через метод:", A.intersection(B))

# Разность A \ B (есть в A, но нет в B)
print("\nРазность A - B:", A - B)
print("Через метод:", A.difference(B))

# Разность B \ A (есть в B, но нет в A)
print("Разность B - A:", B - A)
print("Через метод:", B.difference(A))

# Симметрическая разность (элементы, которые есть только в одном)
print("\nСимметрическая разность A ^ B:", A ^ B)

# Добавляем элемент 9 в A
A.add(9)
print("\nПосле A.add(9):", A)

# Удаляем элемент 3 из A
A.remove(3)
print("После A.remove(3):", A)