# Найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Вариант с While

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

r = 0

while max > min:
    min += 1

    i = min
    f = r
    r = i + f

    if min == max:
        continue

    print(r)

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

f = 0

# Вариант с for

if min > max:
    print("Минимальное число, не должно превышать максимальное")

for i in range(min, max):
    if i == min or i == max:
        continue

    fin = i
    r = f
    f = fin + r

print(f)
