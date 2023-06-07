n = int(input())
max_number = -1
while n!=0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)
