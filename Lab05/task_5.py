# Задание 5. Фильтрация данных
import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 1. Все пассажиры-женщины
female_df = df[df['Sex'] == 'female']
print("Женщин:", len(female_df))

# 2. Все пассажиры старше 30 лет
older_30 = df[df['Age'] > 30]
print("Пассажиров старше 30:", len(older_30))

# 3. Все выжившие
survived_df = df[df['Survived'] == 1]
print("Выживших:", len(survived_df))

# 4. Женщины старше 30 лет (комбинированное условие AND)
female_older_30 = df[(df['Sex'] == 'female') & (df['Age'] > 30)]
print("Женщин старше 30:", len(female_older_30))

# 5. Пассажиры 1-го класса ИЛИ старше 60 лет (условие OR)
class1_or_elderly = df[(df['Pclass'] == 1) | (df['Age'] > 60)]
print("1 класс ИЛИ возраст > 60:", len(class1_or_elderly))

# 6. Порты 'S' или 'C' через isin()
ports_s_c = df[df['Embarked'].isin(['S', 'C'])]
print("Посадка в S или C:", len(ports_s_c))

# 7. Возраст от 20 до 40 через between()
age_20_40 = df[df['Age'].between(20, 40)]
print("Возраст от 20 до 40:", len(age_20_40), "\n")

# 8. Запросы через query()
q1 = df.query("Sex == 'female' and Age > 30")
q2 = df.query("Pclass == 1 or Age > 60")
q3 = df.query("Embarked in ['S', 'C']")
print("Проверка query() (женщины > 30):", len(q1))

# 9. Сколько женщин и мужчин выжило
survived_by_gender = df[df['Survived'] == 1]['Sex'].value_counts()
print("\nКоличество выживших по полу:\n", survived_by_gender)

