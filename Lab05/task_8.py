# Задание 8. Обработка пропусков
import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# 1. Столбцы с пропусками
print("Столбцы с пропусками:\n", df.columns[df.isna().any()].tolist(), "\n")

# 2. Количество пропусков в Age и Cabin
print(f"Пропусков в Age: {df['Age'].isna().sum()}")
print(f"Пропусков в Cabin: {df['Cabin'].isna().sum()}\n")

# 3. Заполнение пропусков в Age медианой
age_median = df['Age'].median()
df['Age'] = df['Age'].fillna(age_median)

# 4. Проверка пропусков в Age
print("Пропусков в Age после fillna:", df['Age'].isna().sum(), "\n")

# 5. Демонстрация dropna() на копии DataFrame
df_copy = pd.read_csv(url)
df_dropped = df_copy.dropna(subset=['Age'])
print("Размер копии после dropna(Age):", df_dropped.shape)

# 6. Заполнение пропусков в Embarked модой
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(embarked_mode)

# 7. Удаление столбца Cabin
df = df.drop(columns=['Cabin'])

# 8. Финальная проверка пропусков
print("\nФинальное количество пропусков по всем столбцам:\n", df.isna().sum())

