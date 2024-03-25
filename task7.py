import json

def to_json(function):
    def wrapped(*args, **kwargs):
        result = function(*args, **kwargs)
        json_parameter = json.dumps(result)
        return json_parameter
    return wrapped

# Функции для примера
@to_json
def difference_numbers(a, b):
    return [f'difference of {a} and {b}',{a : a - b, b : b - a}]

@to_json
def squaring(num):
    return [f'squar of {num} :',{num : num ** 2}]

