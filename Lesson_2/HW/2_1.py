# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


quantity = int(input())
eagle_count = 0
tail_count = 0

for i in range(quantity):
    coin = int(input()) #eagle = 1, tail = 0
    if coin == 1:
        eagle_count += 1
    elif coin == 0:
        tail_count += 1
    else: print("error")
if eagle_count < tail_count:
    print(eagle_count)
else: print(tail_count)