"""Задание 10. Комплексное моделирование: студенты отвечают на тест наугад."""

import numpy as np
import os

# Параметры
np.random.seed(42)
n_students  = 1000
n_questions = 20
p_correct   = 0.25   # вероятность угадать ответ (4 варианта)

print("=" * 50)
print("МОДЕЛИРОВАНИЕ ТЕСТА")
print(f"Студентов: {n_students}, Вопросов: {n_questions}, P(верно): {p_correct}")
print("=" * 50)

# 1. Матрица ответов: каждый элемент — случайное число [0, 1)
answers = np.random.uniform(0, 1, (n_students, n_questions))

# 2. Булева матрица: True если ответ угадан (< p_correct)
correct = answers < p_correct

# 3. Баллы каждого студента (сумма по строкам)
scores = correct.sum(axis=1)

# 4. Статистика
mean_score = scores.mean()
std_score  = scores.std()
print(f"\nСредний балл  : {mean_score:.4f}  (теория: {n_questions * p_correct})")
print(f"Std           : {std_score:.4f}  (теория: ≈ 1.94)")

# 5. Студентов набравших ≥ 10 баллов
passed_10 = np.sum(scores >= 10)
print(f"\nНабрали ≥ 10 баллов : {passed_10} студентов ({passed_10 / 10:.1f}%)")

# 6. «Сдали» тест при пороге 12 баллов
passed_12 = np.sum(scores >= 12)
print(f"Сдали (≥ 12 баллов) : {passed_12} студентов ({passed_12 / 10:.1f}%)")

# 7. Мин/макс баллы
print(f"\nМаксимальный балл : {scores.max()}")
print(f"Минимальный балл  : {scores.min()}")

# 8. Сохраняем и загружаем матрицу ответов
save_path = os.path.join(os.path.dirname(__file__), "answers.npy")
np.save(save_path, answers)
print(f"\n✅ Матрица ответов сохранена в '{save_path}'")

loaded = np.load(save_path)
print(f"✅ Загружена обратно, shape: {loaded.shape}")
print(f"Данные совпадают: {np.array_equal(answers, loaded)}")
