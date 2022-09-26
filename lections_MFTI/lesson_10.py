"""
Реализация бинарного поиска в массиве.
Требование: массив отсортирован.
Разбиваем на границы: левую и правую.
Если искомое число больше, чем максимальное число массива, то получится так, что
правая граница будет указывать на внешний элемент, а левая на крайний.
Скорость поиска О(log2N)
"""

def left_bound(key, a):
    """

    :param key:
    :param a:
    :return:
    """
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right)//2
        if a[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(key, a):
    """

    :param key:
    :param a:
    :return:
    """
    left = -1
    right = len(a)
    while right - left > 1:
        middle = (left + right)//2
        if a[middle] <= key:
            left = middle
        else:
            right = middle
    return left


"""
Динамическое пограммирование.
"""