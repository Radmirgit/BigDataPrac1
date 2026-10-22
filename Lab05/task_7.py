# Задание 7. Сводные таблицы (pivot_table, crosstab)
import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 1. Сводная таблица: средний возраст по Sex и Pclass
pt1 = df.pivot_table(values='Age', index='Sex', columns='Pclass', aggfunc='mean')
print("1. Средний возраст (Sex x Pclass):\n", pt1, "\n")

# 2. Сводная таблица: средняя стоимость билета по Pclass и Embarked
pt2 = df.pivot_table(values='Fare', index='Pclass', columns='Embarked', aggfunc='mean')
print("2. Средняя стоимость билета (Pclass x Embarked):\n", pt2, "\n")

# 3. Сводная таблица: доля выживших по Pclass и Sex
pt3 = df.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean')
print("3. Доля выживших (Pclass x Sex):\n", pt3, "\n")

# 4. crosstab: распределение пассажиров Sex x Pclass
ct1 = pd.crosstab(df['Sex'], df['Pclass'])
print("4. crosstab (Sex x Pclass):\n", ct1, "\n")

# 5. crosstab с процентами по строкам (normalize='index')
ct2 = pd.crosstab(df['Sex'], df['Pclass'], normalize='index') * 100
print("5. crosstab с нормализацией по строкам (%):\n", ct2, "\n")

# 6. Three-way crosstab: Sex по строкам, [Pclass, Survived] по колонкам
ct3 = pd.crosstab(index=df['Sex'], columns=[df['Pclass'], df['Survived']])
print("6. Three-way crosstab (Sex x [Pclass, Survived]):\n", ct3, "\n")

# 7. Сохранение сводной таблицы в CSV
pt3.to_csv('survival_pivot.csv')
print("Сводная таблица 'survival_pivot.csv' сохранена.")

