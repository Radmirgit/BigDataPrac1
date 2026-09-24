"""Задание 5. Списки."""

numbers = [3, 7, 12, 5, 9, 21, 14]
print(numbers[0], numbers[-1], numbers[:3], numbers[1:4])
numbers.append(99)
numbers.insert(2, 0)
numbers.remove(12)
print("После изменений:", numbers)
print("По возрастанию:", sorted(numbers))
print("По убыванию:", sorted(numbers, reverse=True))

s = list(range(10))
print("Срезы:", s[2:7], s[:5], s[5:], s[::2], s[::-1])
print("Квадраты:", [x ** 2 for x in range(1, 11)])
print("Чётные:", [x for x in range(21) if x % 2 == 0])

items = [5, 3, 8, 1]
items.append(10); print("append:", items)
items.extend([20, 30]); print("extend:", items)
items.insert(0, 99); print("insert:", items)
items.remove(99); print("remove:", items)
print("pop:", items.pop(), items)
print("index(8):", items.index(8), "count(3):", items.count(3))
items.sort(); print("sort:", items)
items.reverse(); print("reverse:", items)
