# a = [1, 2, 3, 4, 5]
# for k in range(5):
# a[k] = a[k] * a[k]

# Копирование массива
# N = int(input())
# A = [0] * N
# B = [0] * N
# for k in range(N):
#     A[k] = int(input())
# for k in range(N):
#     B[k] = A[k]


# C = A --это только ссылка на А, С не является списком таким же, как А

# ЛИнейный поиск массива
# def array_search(A: list, N: int, x: int):
#
#     ''' Осуществляетс поиск числа x в массиве A от 0 до N-1 индекса включительно.
#     Возрващает индекс элемента x в массиве A
#     Или -1, если такого нет.
#     Если в массиве несколько одинаковых элементов, равных х, то вернуть индекс первого по счёту'''
#     for k in range(N):
#         if A[k] == x:
#             return k
#     return -1
#
# def test_arraysearch():
#
#     A1 = [1, 2, 3, 4, 5]
#     m = array_search (A1, 5, 8)
#     if m==-1:
#         print('#test1-ok')
#     else:
#         print('#test1- fail')
#
#     A2 = [-1, -2, -3, -4, -5]
#     m = array_search(A2, 5, 8)
#     if m == 2:
#         print('#test1-ok')
#     else:
#         print('#test1- fail')
#
A1 = [1, 2, 3, 4, 5]

def invert_array(A:list, N:int):
    """оБРАЩЕНИЕ мАССИВА (ПОВОРОТ ЗАДОМ-НАПЕРЕД)
    в рамках индексов в рамках от 0 до N-1"""
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    return A
def test_invert_array():
    A1 = [1, 2, 3, 4, 5]

    if A1 == [5, 4, 3, 2, 1]:
        print('#test1- ok')
    else:
        print('#test1- fail')

print(invert_array(A1, 5))