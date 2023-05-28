a = int(input())
num1 = 0
num2 = 1
count = 2

while num2 <= a:
    if num2 == a:
        print(count)
        break
    num1, num2 = num2, num1 + num2
    count += 1
else:
    print(-1)
