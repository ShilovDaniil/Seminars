n = int(input())
quantity_berries = input()
berries = list(map(int, quantity_berries.split()))
max_berries = 0
curr_berries = 0

for i in range(n):
    curr_berries = berries[i] + berries[(i-1)%n] + berries[(i+1)%n]
    if curr_berries > max_berries:
        max_berries = curr_berries

print(max_berries)