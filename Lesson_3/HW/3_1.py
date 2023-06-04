import random

n = int(input())
num = []
for i in range(n):
    num.append(random.randint(1,5))
print(num)
x = int(input())
count = 0
for i in range(len(num)):
    if num[i] == x:
        count+=1

print(count)