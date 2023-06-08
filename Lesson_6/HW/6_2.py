# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list = []
for i in range(10):
    list.append(random.randint(-10,30))
print(list)

lower_limit = 5
upper_limit = 15

for i in range(len(list)):
    if list[i] >= lower_limit and list[i] <= upper_limit:
        print(i)