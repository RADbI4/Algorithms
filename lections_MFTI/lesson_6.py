# Лист компрехеншионс
# A = [x ** 2 for x in range(10)]
# print(A)

# B = []
# for x in A:
#     if x%2 == 0:
#         B.append((x*2))
# B = [x**2 for x in A if x % 2 == 0]
# print(B)
# B = [0 if x < 0 else x**2 for x in A if x % 2 == 0]

# Сортировка массива

"""
Квадратичные сортировка.
Количество операций сортировки N^2
О(N^2) - алгоритм работает не хуже, чем
Инвариант цикла- кусок массива, где все стоят в отсортированными
N-1проход
для сортировки 5 элементов- необходимо 4 действия
N- размер массива
"""

"""
1)Сортировка вставками(Insert sort)
1+2+3+4=10
Не привышает (N*(N-1))/2  
"""
A = [4, 2, 5, 1, 3]


def insert_sort(A):
    '''
    Сортировка списка А вставками

    :param A:
    :return:
    '''
    pass


'''
2)Сортировка методом выбора
Choice Sort
Не проходить в поиске минимума в том месте, где массив уже отсортирован
среди оставшихся найтиминимум и поставить его на вакантное место.
С каждым отсортированным элементом необходимо увеличивать значение отсортирвоанности.
Последнего сортировать не надо
'''
# A = [4, 2, 5, 1, 3]
"""
3)Метод пузыря
Bubble sort
Сортировать 2 соседних элемента, начиная с начала
Инвариант: 
Самый бошльшой элемент отправляется в конец массива, всплывая как пузырёк.
Поэтомоу последнего необязательно сортировать. С каждым разом надо всё меньше сортировать.
Требуется 3 сравнения в этом случае
на 1 проходе 4 сравнения, потом 3, 2 и 1, всего 10 сравнений. Арифметическая прогрессия.
4+3+2+1=10
1+2+...(N-1)=(N*(N-1))/2
"""


# A = [4, 2, 5, 1, 3]

def buble_sort(A):
    '''
    Сортировка А пузрём
    :param A:
    :return:
    '''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


def choise_sort(A):
    '''
    Сортировка А выбором
    :param A:
    :return:
    '''
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def inserted_sort(A):
    '''
    Сортировка А вставками
    :param A:
    :return:
    '''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print('Testcase#1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    """Сравнение двух списков- затратно по ресурсам лен А операций это долго"""
    print('OK' if A == A_sorted else "Fail")

    print('Testcase#2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else "Fail")

    print('Testcase#3: ', end='')
    A = [1, 2, 4, 4, 2]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else "Fail")
    pass


if __name__ == "__main__":
    test_sort(inserted_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)

'''Testing drive development'''


