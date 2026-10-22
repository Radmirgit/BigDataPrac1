# Задание 1. Series: создание и свойства
import pandas as pd
import numpy as np

# 1-3. Создание Series из списков
s1 = pd.Series([10, 20, 30, 40, 50])
print("Series 1:\n", s1, "\n")

s2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Series 2:\n", s2, "\n")

# 4-5. Series из словаря с именами объекта и индекса
grades_data = {'Математика': 5, 'Физика': 4, 'История': 3, 'Информатика': 5}
s3 = pd.Series(grades_data)
s3.name = 'Оценки студента'
s3.index.name = 'Предметы'
print("Series 3 (Оценки):\n", s3, "\n")

# 6. Доступ по метке и позиции
print("Оценка по метке 'Математика':", s3['Математика'])
print("Оценка по позиции [0]:", s3.iloc[0], "\n")

# 7. Диагностика через info() и describe()
print("--- info() и describe() ---")
print("s1 describe:\n", s1.describe(), "\n")
print("s2 describe:\n", s2.describe(), "\n")
print("s3 describe:\n", s3.describe(), "\n")
print("s3 info:")
s3.info()
print()

# 8. Векторизованное умножение на 2
s3_doubled = s3 * 2
print("Оценки, умноженные на 2:\n", s3_doubled, "\n")

# 9. Фильтрация: значения с оценкой 5
print("Предметы с оценкой 5:\n", s3[s3 == 5])
