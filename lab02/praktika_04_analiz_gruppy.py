students = [
    {'name': 'Аня', 'grades': [5, 4, 5]},
    {'name': 'Борис', 'grades': [3, 3, 4]},
    {'name': 'Влад', 'grades': [4, 5, 4]},
    {'name': 'Даша', 'grades': [5, 5, 5]},
    {'name': 'Егор', 'grades': [3, 4, 3]}
]

for s in students:
    avg = sum(s['grades'])/len(s['grades'])
    print(s['name'], avg)

best = max(students,
key=lambda x: sum(x['grades']))
worst = min(students,
key=lambda x: sum(x['grades']))

group_avg = sum(sum(s['grades'])/len(s['grades']) for s in students) / len(students)
print('Лучший:', best['name'])
print('Худший:', worst['name'])
print('Средний балл группы:', group_avg)

above_avg = [s['name'] for s in students if sum(s['grades'])/len(s['grades']) > group_avg]
print('Выше среднего:', above_avg)

students_sorted = sorted(students, key=lambda x: sum(x['grades'])/len(x['grades']), reverse=True)

with open('group_report.txt', 'w', encoding='utf-8') as f:
    f.write(f"Средний балл группы: {group_avg}\n")
    f.write(f"Лучший: {best['name']}\n")
    f.write(f"Худший: {worst['name']}\n")
    for s in students_sorted:
        f.write(f"{s['name']}: {sum(s['grades'])/len(s['grades'])}\n")

# files.download('group_report.txt') # для Google Colab
