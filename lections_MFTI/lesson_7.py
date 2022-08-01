import graphics_pack as gr

"""Recurison
Вспомни сказку про репку, где каждый последующий персонаж дёргает репку.
Репка вызывает деда и даёт ему входные данные, и вызывает деда, дед вызывает бабку и даёт ей свои входные данные,
бабушка вызызвает дочку и даёт ей свои выходные данные и так далее- Это всё стэк вызывов Call Stack.
Репка, дед, бабушка и остальные персонажи- это подпрограммы.
Подзадача дорлжна быть проще задачи. ОЧЕНЬ ВАЖНО! Всегда должен быть крайний случай. Любой Другшой случай- рекурентный.

Другой пример: матрёшка.
Изготовить матрёшку. С уровнем вложенности 5. (Т.е. 5 матрешек).
Изгтавливаем верх и низ и надо засунуть туда матрёшку с вложенностью 4, но сам мастер не делает это, он даёт другу
её изготовить, тот поступает точно так же, изготавливая матрешку с уровнем заполненности 3 и так далее до 0.
Мастера- подпрограммы, которые дают задачу для другой задачи и упрощается до последней матрёшки, колторая не
разделяется.
Далее происходит возврат, обратное действие. Каждая подпрограмма ждёт выполнения предидущей, матрёшки встают друг
в друга.

Переполнение стэка вызывов. У рекурсии обязательно должен быть:
а) Рекуретный случай. (Способ его обработки)
б) Крайний случай. (КОнечный случай)

Рекурсию писать нельзя без условий выше!

Рекурсия не всегда нужна. Повторяющиецйся, циклический характер действия. Тут нет задачи, решающей другую задачу. Они
циклические.
"""

"""
Матрёшка.
Первым делом определяем последний случай, Крайний случай!
"""


# def matryoshka(n):
#     """
#     Рекурсивная функция сбора матрёшки
#     :param n:
#     :return:
#     """
#     if n == 1:
#         print('Матрёшка!')
#     else:
#         print(f'Верх матрёшки n= {n}')
#         matryoshka(n - 1)
#         print(f'Низ матрёшки n= {n}')


'''
У каждой рекурсивной функции при работе своё пространство, поддерживает имена, когда она ретёрн, то это пространство и
её имена- стираются. Мастера существуют только тогда, когда фукция работает.
'''

'''
Задача на построение графика функции квадрата. Квадрат внутри квадрата, где каждая сторона на 0.4 меньше.
Фрактало подобное нечто))))

AA1 = alpha * AB

Глубина рекурсии- есть количестиво самовызовов функции, включая первый. 
Глубина увеличивается.
'''

'''
Для каждой программы должны быть граничные условия, которые проверяются на входе.
f(n) = 1, n=0
f(n)*n, n=>1
'''

#
# def f(n: int):
#     """
#     Рекурсионный факториал числа
#     :param n:
#     :return:
#     """
#
#     if n <= 1:
#         assert n >= 0, 'Факториал отриц. не опредлён!'  # Вызывет ошибку, если функция вызвана с неправильнывм параметром
#         if n == 0:
#             return 1
#         return f(n - 1) * n


'''
Алгоритм Евклида.
предполагается а > б
2 числа А и Б. Наибольший общий делитель? Наибольшее целое число, на которое можно поделить А и Б нацело.
НОД(А, Б) 
(а-б)::д
а можно заменить на а-б
НОД(А, Б) = НОД(А, Б) (a-b,b)
gcd(a,b) = 
1)a, a=b
Два рекурентных случая:
2)gcd(a-b, b), a-b
3)gcd(a,b-a), b > a
'''


# def gcd(a, b):
#     if a == b:
#         return a
#     elif a > b:
#         return gcd(a - b, b)
#     else:  # a < b
#         'Призрак- какое то место в программе точно выполняется, ты в этом уверен и по другому быть не должно. ' \
#         'В этом случае должно быть комментирование, либо assertion' \
#         'Тут нет присваивания' \
#         'Улучшаем логику НОД(А, Б) = НОД(А, Б) (a % b, b)' \
#         'НОД(А, Б) = НОД(А, Б) (b % a, b)' \
#         'Два рекурентных случая: ' \
#         '1)a, b= 0, a-b 2' \
#         '2)gcd(b,a%b)'
#         return gcd(a, b - a)
#
#
# def gcd_improoved(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd_improoved(b, a % b)
#
#
# def gcd_improoved_x2(a, b):
#     return a if b == 0 else gcd_improoved_x2(b, a % b)


'''
Рекурсивное возведение в степень. Быстрое.
a(n) = a*a*a*a*a*a....n раз - суть в математике. Задача вычисления более сложного числа.
Рекуретное рассуждение: a^n= a^(n-1) - задача вычисления меньшей степени
Если n-отриц-ое, то мы ухудшаем задачу.
Крайний случай a^0=1
'''


# def pow (a: float, n: int):
#     """
#     pow(a,n) =
#     1, n = 0
#     2, pow(a, n-1)*a, n > 0
#     :param a:
#     :param n:
#     :return:
#     """
#     return 1 if n == 0 else pow(a, n-1)*a

'''
Если а оказалось в чётной степени a^2k = (a^2)^k
a^n=(a^2)^(n/2)
'''


# def pow2 (a: float, n: int):
#     """
#     Каждая следущая рекурсия уменьшает необходимую для вычисления степень, так как она понижается.
#     pow(a,n) =
#     1, n = 0
#     2, pow(a, n-1)*a, n не чёт
#     3, pow(a**2, n//2), n чёт
#     :param a:
#     :param n:
#     :return:
#     """
#     if n == 0:
#         return 1
#     elif n % 2 == 1: #нечётная степень
#         return pow(a, n-1)*a
#     else: #n- чётное
#         return pow(a**2, n//2)


"""
Ханойские башни.
3 Башни с блинчиками.
Все блинчики на 1 башне.
Надо переложить все блинчики по 1 (нельзя хвататься за 2 сразу).
С 1 столбца переложить на 2ой, нельзя по 2, нельзя блинчик большего диаметра лежал на блинчике меньшего.
Сводим задачу к решенной.
Пирадмидка размером 1- крайний случай.
На некотором к-ом столбике лежит блин размера n, над этим блином nлежит пирамидка из n-1 блинов.
Я умею переложить такую пирамиду, но предложу другу (другой функции) дорогой переложи на 3ий столбик tmp.
k + i + tmp = 1 + 2 +3 = 6 3 столбика столбика
tmp = 6 - k - i - дискретная математикаю
Друг переложил пирамидку в tmp.
И мы оставшийся 1 блин перекладываем с к-ого на i-ый столбец.
Друг а ты n-1 поставь пирамидку сверху на временный на целевой столлбец i.
Если мы можем переложить меньшего размера. то я могу передвинуть пирамиду большего размера.
"""

# if __name__ == "__main__":
# matryoshka(5)

print(f"Среднее значение комнат= {np.mean(CDF['Rooms'])} \n "
      f"Среднее значение общей площади= {np.mean(CDF['Square'])}")