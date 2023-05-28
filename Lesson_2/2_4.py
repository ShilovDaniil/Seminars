quantity = int(input())
min_weigth = 999
max_weigth = 0

for i in range(quantity):
    watermelon = int(input())
    if watermelon > max_weigth:
        max_weigth = watermelon
    elif watermelon < min_weigth:
        min_weigth = watermelon

print (max_weigth, min_weigth)