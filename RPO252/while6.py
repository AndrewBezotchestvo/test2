import random

lifes = 3
score = 0

while  lifes > 0:
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)

    print(num1, "+", num2, "=", end=" ")
    answer = int(input())

    if answer == num1 + num2:
        print("Верно")
        score += 1
    else:
        print("Не верно, - 1 жизнь")
        lifes -= 1

print("Ваш счет: ", score)
