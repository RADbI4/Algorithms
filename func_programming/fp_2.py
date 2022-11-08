"""
Продолжаю практиковаться в функциональном программировании
Continue practicing in function style of programming
"""
from functools import reduce, partial
from datetime import datetime


# Функция простой операции умножения на 2 для того, чтобы понять, как это работает.
# Simple function of multiple to understad how it works
multiply = lambda *args: reduce(lambda x1, x2: sum((x1, x2)) * 2, *args)

# Функция простой операции сложения для того, чтобы понять, как это работает.
# Simple function of add to understad how it works
add = lambda *args: reduce(lambda x1, x2: tuple([(x1 + x2) / 2] + [(x1 + x2) / 2]), *args)

# Функция простой операции вычитания для того, чтобы понять, как это работает.
# Simple function of substraction to understad how it works
minus = partial(lambda x1, x2: x1 - x2, x2=2)

test_data = (1, 2)

"""
Теперь, чтобы не писать minus(multiply(add(test_data)), 2), 
я сделаю функцию, которая это сделает сама, последовательно, передавая результат одной функции в другую.
Она должна выглядеть примерно так: attractor(add, multiply, minus)(test_data)
"""
# Первая версия аттрактора, а если я хочу больше, чем 2 функции?
attractor_1 = lambda *args: lambda a, b: b(a(*args))

"""
Имплозивный Аттрактор. 

Подобно чёрной дыре поглащает аргументы и функции. 

Когда очередная функция выполнила вычисления, он
немедленно отправляет результаты вычисления в следующую функцию как аргументы, проваливаясь внутрь самого
себя до тех пор, пока последняя функция в списке не вернёт свои значения- это и будет тем, что выведет Аттрактор.

Для того, чтобы функция работала правильно- необходимо знать сколько аргументов принимает текущая функция, 
сколько она их возвращает и какие аргументы принимает след. функция.
Если цепочка нарушается, то имплозия не происходит и интерпретатор вернёт ошибку.

Аттрактор делает код удобнее к чтению, а каждую отдельно взятую функцию легче тестировать, чем один большой скрипт.

implosive_attractor(test_data, funcs=[add, multiply, minus]) 

Тут сразу видно что, мы берём test_data, и последовательно сначала складываем их, потом умножаем ответ на 2 и вычитаем
из ответа 2.
"""
implosive_attractor = lambda *args, funcs: reduce(lambda a, b: b(a), funcs, funcs[0](*args))




if __name__ == "__main__":
    start_time = datetime.now()

    print(add(test_data))

    print(multiply(add(test_data)))

    print(minus(multiply(add(test_data))))

    print(attractor_1(test_data)(add, multiply))

    print(implosive_attractor(test_data, funcs=[add, multiply, minus]))

    # print(attractor(add, multiply, minus)(test_data))

    print(datetime.now() - start_time)
    pass
