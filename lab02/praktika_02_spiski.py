import random

lst = [random.randint(1, 100)
for _ in range(10)]

print(lst)
print('Min:', min(lst))
print('Max:', max(lst))
print('Sum:', sum(lst))
print('Avg:', sum(lst)/len(lst))

lst.sort()
lst.sort(reverse=True)
print(lst[:3], lst[-3:])
print(lst[::-1])
lst.append(100); lst.pop(5)
