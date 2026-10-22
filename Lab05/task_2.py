# Задание 2. DataFrame: создание и свойства
import pandas as pd
import numpy as np

# 1. Создание DataFrame из словаря
data = {
    'ФИО': ['Иванов', 'Петров', 'Сидоров', 'Кузнецова', 'Смирнов'],
    'Математика': [5, 3, 4, 5, 4],
    'Физика':     [4, 5, 5, 4, 3],
    'История':    [5, 4, 5, 3, 5],
    'Информатика':[4, 5, 3, 5, 4]
}
df = pd.DataFrame(data)

# 2. Вывод DataFrame целиком
print("Исходный DataFrame:\n", df, "\n")

# 3. Атрибуты структуры
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index)
print("Dtypes:\n", df.dtypes, "\n")

# 4-5. Первые 3 и последние 2 строки
print("head(3):\n", df.head(3), "\n")
print("tail(2):\n", df.tail(2), "\n")

# 6. Задание имён индексу и столбцам
df.index.name = 'Студенты'
df.columns.name = 'Предметы'
print("DataFrame с именованными осями:\n", df, "\n")

# 7. info() и describe()
print("DataFrame info:")
df.info()
print("\nDataFrame describe:\n", df.describe(), "\n")

# 8. Сортировка по Математике по убыванию
df_sorted = df.sort_values(by='Математика', ascending=False)
print("Сортировка по Математике (убывание):\n", df_sorted, "\n")

# 9. Добавление столбца со средним баллом
subjects = ['Математика', 'Физика', 'История', 'Информатика']
df['Средний балл'] = df[subjects].mean(axis=1)
print("DataFrame с новым столбцом 'Средний балл':\n", df)

