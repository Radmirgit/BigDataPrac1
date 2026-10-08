"""Лабораторная работа №2. Дополнительные задания (Домашнее задание)."""

# 1. Функция: список -> список квадратов
def square_list(lst):
    return [x ** 2 for x in lst]

# 2. Словарь частот слов в тексте
def word_frequencies(text):
    freq = {}
    words = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

# 3. Игра «Угадай число» (демонстрационная функция с ограничением попыток)
def guess_number_simulated(target, guesses):
    print(f"--- Игра «Угадай число» (загадано {target}) ---")
    for g in guesses:
        print(f"Попытка: {g}")
        if g == target:
            print("Поздравляем! Число угадано!")
            return True
        elif g < target:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
    return False

# 4. Проверка палиндрома
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# 5. Удаление дубликатов из 20 чисел
import random

def remove_duplicates_demo():
    numbers = [random.randint(1, 15) for _ in range(20)]
    unique_numbers = list(dict.fromkeys(numbers)) # сохраняет порядок элементов
    return numbers, unique_numbers


if __name__ == "__main__":
    print("1. Квадраты списка [1..5]:", square_list([1, 2, 3, 4, 5]))
    
    text = "Python это просто и Python это мощно"
    print("2. Частоты слов:", word_frequencies(text))
    
    print("\n3. Тест игры «Угадай число»:")
    guess_number_simulated(42, [20, 50, 42])
    
    print("\n4. Проверка палиндрома:")
    for test_word in ["А роза упала на лапу Азора", "Привет"]:
        print(f"  '{test_word}': {is_palindrome(test_word)}")
        
    orig, uniq = remove_duplicates_demo()
    print("\n5. Удаление дубликатов:")
    print("  Исходные (20):", orig)
    print("  Уникальные   :", uniq)
