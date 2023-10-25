try:
    a = int(input("Введите число: "))
    b = 0
    c = 0
    while a > 0:
        if a % 2 == 0:
            b = b + 1
        else:
            c = c + 1
        a = a // 10
    print("Четные:", b)
    print("Нечетные:", c)
except ValueError:
    print("Ошибка: Введите целое число.")