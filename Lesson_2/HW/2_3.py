# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

n = int(input())
k = 0
result = 2 ** k

while result < n:
    print(result)
    k+=1
    result = 2 ** k