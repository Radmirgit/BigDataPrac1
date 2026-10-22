# Задание 4. Импорт данных из CSV и диагностика
import pandas as pd

# 1-2. Загрузка Titanic по URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 3. Первые 5 и последние 5 строк
print("Первые 5 строк:\n", df.head(5), "\n")
print("Последние 5 строк:\n", df.tail(5), "\n")

# 4. Диагностика структуры
print("--- info() ---")
df.info()
print()

# 5. Статистическое описание
print("describe() для числовых признаков:\n", df.describe(), "\n")
print("describe(include=['object']) для категориальных признаков:\n", df.describe(include=['object']), "\n")

# 6. Подсчет пропусков в каждом столбце
missing_values = df.isna().sum()
print("Пропуски по столбцам:\n", missing_values, "\n")

# 7. Процент пропусков в столбце Age
age_missing_pct = (df['Age'].isna().sum() / len(df)) * 100
print(f"Процент пропусков в Age: {age_missing_pct:.2f}%\n")

# 8. Вывод только столбцов Name, Age, Survived
print("Выборка Name, Age, Survived:\n", df[['Name', 'Age', 'Survived']].head(), "\n")

# 9. Переименование столбца Sex в Gender
df = df.rename(columns={'Sex': 'Gender'})
print("Столбцы после переименования:\n", df.columns.tolist())

