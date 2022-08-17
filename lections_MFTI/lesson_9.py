"""
Сортировка слиянием. Быстрая сортировка.

Сортировка слиянием. (Слияние отсортированных массивов в один).

Сортировка называется устойчивой, если она не меняет порядок равных элементов.
"""


def merge(a: list, b: list):
    """
    i- индекс а
    k- индекс b
    n-индекс с
    :param a:
    :param b:
    :return:
    """
    i = 0
    k = 0
    n = 0
    c = [0] * (len(a) + len(b))
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1

    return c


'''
Рекуретная функция merge_sort
'''


def merge_sort(a):
    '''
    :param a:
    :return:
    '''

    if len(a) <= 1:
        return
    middle = len(a) // 2
    l = [a[i] for i in range(0, middle)]
    r = [a[i] for i in range(middle, len(a))]
    merge_sort(l)
    merge_sort(r)
    c = merge(l, r)
    for i in range(len(a)):
        a[i] = c[i]


"""
Сортировка ТониХоара
"""


def hoar_sort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    l = []
    m = []
    r = []
    for x in a:
        if x < barrier:
            l.append(x)
        elif x == barrier:
            m.append(x)
        else:
            r.append(x)
    hoar_sort(l)
    hoar_sort(r)
    k = 0
    for x in l + m + r:
        a[k] = x
        k += 1


"""
Проверка на сортированность массива.
"""


def check_sorted(a, asccending=True):
    '''
    Провряет отсортированн ли массив или нет. За o(len(a))
    :param a:
    :param asccending:
    :return:
    '''
    flg = True
    s = 2 * int(asccending)
    n = len(a)
    for i in range(0, n - 1):
        if s * a[i] > s * a[i + 1]:
            flg = False
            break
    return flg


"""
Бинарный поиск в массиве.
Если массив отсортирован?
[1,2,2,2,2,3,4,5,5,5,5,5,7,7,7,7,7]
Надо найти 5?
А если 6?
6 нет в массиве.
Если ищем 5, то нужно в таком случае указать границы левой и праввой 5.
Если ищем 6, то правая граница будет указывать на правый элемент от 6, а левая граница на леввый.
Если ищем 7 , то в таком случае толь левая граница.
Левая граница не левее, чем -1, а правая граница не правее, чем n.

Логика двоичного поиска:
middle = (left + right)//2
сравниванием этот элемент с искомым.
Эта середина становится одним из краёв.
"""
