import functools
from datetime import datetime

def decorater(function):
  @functools.wraps(function)
  def wrapped(*args, **kwargs):
    result = function(*args, **kwargs)
    with open(f'{function.__name__}', 'a') as f:
      print(datetime.now(), result, file=f)
    return result 
  return wrapped

@decorater
def difference_numbers(a, b):
    return {a : a - b, b : b - a}

@decorater
def squaring(num):
    return {num : num ** 2}

print(difference_numbers(2, 3))
print(squaring(3))