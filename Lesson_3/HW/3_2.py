import random

n = int(input())
num = []
for i in range(n):
    num.append(random.randint(1,5))
print(num)
x = int(input())
answer = num[0]
for i in range(1, n):
    if (num[i] - x) ** 2 < (answer - x) ** 2:
        answer = num[i]
print(answer)