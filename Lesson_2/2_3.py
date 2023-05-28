n = int(input())
count = 0
max_count = 0

for n in range(n):
    temp = int(input())
    if temp > 0:
        count+=1
    elif temp <= 0:
        count = 0
    elif count > max_count:
        max_count = count
print(max_count)