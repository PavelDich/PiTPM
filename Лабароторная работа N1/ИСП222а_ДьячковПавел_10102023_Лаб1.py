+\

    NoTask = int(input('Вывести блок "1-10". Вывести все блоки "0". Закончить цикл "-1": '))
while True:
    # Блок 1
    if NoTask == 1 or NoTask == 0:
        print("\n Блок 1")

        # Задача 1 «Площадь прямоугольного треугольника»
        print('\n Задача 1 «Площадь прямоугольного треугольника»')
        a = int(input())
        b = int(input())
        c = int(input())
        print(a + b + c)

        # Задача 2 «Площадь прямоугольного треугольника»
        print('\n Задача 2 «Площадь прямоугольного треугольника»')

        h = float(input())
        b = float(input())
        print(b * h * 0.5)

        # Задача 3 «Дележ яблок»
        print('\n Задача 3 «Дележ яблок»')

        n = int(input())
        k = int(input())
        a = k // n
        b = k - a * n
        print(str(a) + "\n" + str(b))

        # Задача 4 «Электронные часы»
        print('\n Задача 4 «Электронные часы»')

        n = int(input())
        print(n % (60 * 24) // 60, n % 60)

        # Задача 5 «Hello, Harry!»
        print('\n Задача 5 «Hello, Harry!»')

        a = str(input())
        print("Hello,", a + "!")

    # Блок 2
    if NoTask == 2 or NoTask == 0:
        print("\n Блок 2")

        # Задача 1 «Яша плавает в бассейне»
        print('\n Задача 1 «Яша плавает в бассейне»')

        N = int(input())
        M = int(input())
        x = int(input())
        y = int(input())
        if x > (N - x) and N >= x:
            x = (N - x)
        elif x > (M - x):
            x = (M - x)

        if y > (N - y) and N >= y:
            y = (N - y)
        elif y > (M - y):
            y = (M - y)

        if y > x:
            print(x)
        else:
            print(y)

        # Задача 2 «Шоколадка»
        print('\n Задача 2 «Шоколадка»')

        n = int(input())
        m = int(input())
        k = int(input())
        if ((k % n) == 0 or (k % m) == 0) and k <= n * m:
            print("YES")
        else:
            print("NO")

        # Задача 3 «Ход коня»
        print('\n Задача 3 «Ход коня»')

        columnA = int(input())
        lineA = int(input())
        columnB = int(input())
        lineB = int(input())

        if columnA - columnB == 2 or columnA - columnB == -2:
            if lineA - lineB == 1 or lineA - lineB == -1:
                print("YES")
            else:
                print("NO")
        elif columnA - columnB == 1 or columnA - columnB == -1:
            if lineA - lineB == 2 or lineA - lineB == -2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")

        # Задача 4 «Ход ферзя»
        print('\n Задача 4 «Ход ферзя»')

        columnA = int(input())
        lineA = int(input())
        columnB = int(input())
        lineB = int(input())

        if columnA - columnB == lineA - lineB or columnA - columnB == -(lineA - lineB):
            print("YES")
        elif columnA - columnB == 0 or lineA - lineB == 0:
            print("YES")
        else:
            print("NO")

        # Задача 5 «Ход слона»
        print('\n Задача 5 «Ход слона»')

        columnA = int(input())
        lineA = int(input())
        columnB = int(input())
        lineB = int(input())

        if columnA - columnB == lineA - lineB or columnA - columnB == -(lineA - lineB):
            print("YES")
        else:
            print("NO")

        # Задача 6 «Ход короля»
        print('\n Задача 6 «Ход короля»')

        columnA = int(input())
        lineA = int(input())
        columnB = int(input())
        lineB = int(input())

        if columnA - columnB == 1 or columnA - columnB == -1:
            if (lineA - lineB == 1 or lineA - lineB == -1 or lineA - lineB == 0):
                print("YES")
        elif lineA - lineB == 1 or lineA - lineB == -1:
            if (columnA - columnB == 1 or columnA - columnB == -1 or columnA - columnB == 0):
                print("YES")
        else:
            print("NO")

        # Задача 7 «Ход ладьи»
        print('\n Задача 7 «Ход ладьи»')

        columnA = int(input())
        lineA = int(input())
        columnB = int(input())
        lineB = int(input())

        if columnA - columnB == 0 or lineA - lineB == 0:
            print("YES")
        else:
            print("NO")

        # Задача 8 «Сколько совпадает чисел»
        print('\n Задача 8 «Сколько совпадает чисел»')
        number1 = int(input())
        number2 = int(input())
        number3 = int(input())
        a = 0

        if number1 == number2 == number3:
            print(3)
        elif number1 == number2 or number1 == number3 or number2 == number3:
            print(2)
        else:
            print(0)

        # Плюс: 1
        print('\n Плюс: 1')
        number = int(input())
        if abs(number) % 2 == 0:
            print("Четное")
        else:
            print("Нечентное")

    # Блок 3
    if NoTask == 3 or NoTask == 0:
        print("\n Блок 3")

        # Задача 1 «Последняя цифра числа»
        print('\n Задача 1 «Последняя цифра числа»')
        number = int(input())
        lastNum = str(number)[-1]
        print(lastNum)

        # Задача 2 «МКАД»
        print('\n Задача 2 «МКАД»')
        speed = float(input())
        time = float(input())
        print(round(109 + speed * time) % 109, 0)

        # Задача 3 «Дробная часть»
        print('\n Задача 3 «Дробная часть»')
        x = float(input())
        temp = str(x)
        point = temp.find('.')
        x = float(temp[point:len(temp)])
        print(x)

        # Задача 4 «Первая цифра после точки»
        print('\n Задача 4 «Первая цифра после точки»')
        x = float(input())
        x = str(int(x * 10) % 10)
        print(x)

        # Задача 5 «Конец уроков»
        print('\n Задача 5 «Конец уроков»')
        a = int(input())
        a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
        print(a // 60 + 9, a % 60)

        # Задача 6 «Автопробег»
        print('\n Задача 6 «Автопробег»')
        n = int(input())
        m = int(input())
        print((m + n - 1) // n)

        # Задача 7 «Стоимость покупки»
        print('\n Задача 7 «Стоимость покупки»')
        a = int(input())
        b = int(input())
        n = int(input())
        c = (a * 100 + b) * n
        print(c // 100, c % 100)

        # Задача 8 «Разность времен»
        print('\n Задача 8 «Разность времен»')
        h1 = int(input())
        m1 = int(input())
        s1 = int(input())
        h2 = int(input())
        m2 = int(input())
        s2 = int(input())
        print((s2 + (m2 * 60) + (h2 * 60 * 60)) - (s1 + (m1 * 60) + (h1 * 60 * 60)))

        # Плюс: 1
        print('\n Плюс: 1')
        x = int(input())
        m = ""
        if x % 3 == 0:
            m += "Bang"
            if x % 5 == 0:
                m += "Boom"
        else:
            m = "Miss"
        print(m)

    # Блок 4
    if NoTask == 4 or NoTask == 0:
        print("\n Блок 4")

        # Задача 1 «Дано натуральное число. Выведите его последнюю цифру»
        print('\n Задача 1 «Дано натуральное число. Выведите его последнюю цифру»')






    if NoTask == -1:
        break

    NoTask = int(input('Вывести блок "1-10". Вывести все блоки "0". Закончить цикл "-1": '))
