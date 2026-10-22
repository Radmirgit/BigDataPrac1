# Задание 9. Комплексный анализ Titanic
import pandas as pd

# Загрузка и предварительная очистка из Задания 8
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])

# 1. Признак FamilySize = SibSp + Parch + 1
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 2. Признак IsAlone (1 если FamilySize == 1, иначе 0)
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

# 3. Доля выживших для одиночек и для пассажиров с семьей
survival_alone = df.groupby('IsAlone')['Survived'].mean()
print("Доля выживших (0 - с семьей, 1 - один):\n", survival_alone, "\n")

# 4. Средний возраст выживших и погибших
age_by_survival = df.groupby('Survived')['Age'].mean()
print("Средний возраст (0 - погиб, 1 - выжил):\n", age_by_survival, "\n")

# 5. Сводная таблица выживаемости по Sex x Pclass
pivot_survival = df.pivot_table(values='Survived', index='Sex', columns='Pclass', aggfunc='mean')
print("Сводная таблица выживаемости (Sex x Pclass):\n", pivot_survival, "\n")

# 6. Топ-5 самых дорогих билетов и их выживаемость
top5_fare = df.nlargest(5, 'Fare')
print("Топ-5 самых дорогих билетов:\n", top5_fare[['Name', 'Fare', 'Survived']])
print(f"Доля выживших среди топ-5: {top5_fare['Survived'].mean() * 100:.1f}%\n")

# 7. Средний возраст по классам
print("Средний возраст по классам:\n", df.groupby('Pclass')['Age'].mean(), "\n")

# 8. Сохранение очищенного датасета
df.to_csv('titanic_clean.csv', index=False)
print("Файл 'titanic_clean.csv' успешно сохранен.")

