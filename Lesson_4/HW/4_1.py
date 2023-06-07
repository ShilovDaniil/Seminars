n = int(input())
m = int(input())

set_n = set()
set_m = set()

for i in range(n):
    set_n.add(int(input()))
for j in range(m):
    set_m.add(int(input()))

print(set_n)
print(set_m)

common_numbers = list(set_n.intersection(set_m))
common_numbers.sort()

for num in common_numbers:
    print(num)