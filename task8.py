from datetime import datetime
import sys

def decorator(function):
    def wrapped(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except Exception:
            exception_type =  sys.exc_info()[1]
            with open(f'{function.__name__}', 'a') as file:
                file.write(f'{datetime.now()} Вид исключения: {exception_type}')
                return exception_type
    return wrapped

@decorator
def difference_of_num(a, b):
    return {'Разность a - b' : a[0] - b, 'Разность b - a' : b - a }

@decorator
def squaring_num(num):
    return { 'Квадрат' : (num ** 2) / 0}

