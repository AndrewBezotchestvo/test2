# 4. Дано число k. Вычислите сумму квадратов
# нечетных чисел от 1 до k.

k = 5
i = 1
summa = 0

while i <= k:
    if i % 2 != 0:
        summa += i ** 2
    i += 1

print(summa)