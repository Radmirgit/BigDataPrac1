s = {
'name': 'Иван', 'age': 20,
'city': 'Москва',
'grades': [5, 4, 3, 5, 4]
}
s['university'] = 'МГУ'
s['age'] = 21
avg = sum(s['grades'])/len(s['grades'])
s['grades'].append(5)
del s['city']
for k, v in s.items(): print(k, v)
print('email' in s) # False
