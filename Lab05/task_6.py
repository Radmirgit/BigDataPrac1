# Задание 6. Группировка и агрегация (groupby)
import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 1. Средний возраст по полу
print("Средний возраст по полу:\n", df.groupby('Sex')['Age'].mean(), "\n")

# 2. Средняя стоимость билета по классу
print("Средняя стоимость билета по классу:\n", df.groupby('Pclass')['Fare'].mean(), "\n")

# 3. Количество пассажиров в каждом порту
print("Пассажиров по портам (Embarked):\n", df.groupby('Embarked')['PassengerId'].count(), "\n")

# 4. Стандартное отклонение возраста по классу
print("Стандартное отклонение возраста по классу:\n", df.groupby('Pclass')['Age'].std(), "\n")

# 5. Средний возраст и Fare одновременно через agg()
print("Средние Age и Fare по классу:\n", df.groupby('Pclass')[['Age', 'Fare']].mean(), "\n")

# 6. Набор метрик для Fare по классам
print("Метрики для Fare по классам:\n", df.groupby('Pclass')['Fare'].agg(['mean', 'std', 'min', 'max']), "\n")

# 7. Именованные агрегации
named_agg = df.groupby('Pclass').agg(
    avg_age=('Age', 'mean'),
    avg_fare=('Fare', 'mean')
)
print("Именованные агрегации:\n", named_agg, "\n")

# 8. Группировка по Pclass и Sex — средняя выживаемость
survival_rate = df.groupby(['Pclass', 'Sex'])['Survived'].mean()
print("Выживаемость по Pclass и Sex:\n", survival_rate, "\n")

# 9. Количество пассажиров Pclass x Sex
passengers_count = df.groupby(['Pclass', 'Sex'])['PassengerId'].count()
print("Количество пассажиров Pclass x Sex:\n", passengers_count)

