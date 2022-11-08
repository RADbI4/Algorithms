"""
Тут сосредоточены мои полезные функции.
There will be my own helpful funcs
"""
from functools import partial, reduce
from datetime import datetime
import decimal as Decimal
import traceback

constructor = lambda last_func, primary_func: lambda *args: partial(last_func(primary_func(*args)))

list_engine = constructor(list, map)

zip_engine = constructor(dict, zip)
filter_engine = constructor(list, filter)

if __name__ == "__main__":
    start_time = datetime.now()

    print(datetime.now() - start_time)
    pass
