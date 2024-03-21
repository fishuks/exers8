import functools

def suitable_numbers(numbers, c):
    suitabl_list = []
    for number in numbers:
        if (number**0.5).is_integer() and number % c == 0:
            suitabl_list.append(number)
    return suitabl_list

a = int(input())
b = int(input())
c = int(input())
numbers = range(a, b + 1)
print(suitable_numbers(numbers, c))
result = functools.reduce(lambda x,y : x + y, suitable_numbers(numbers, c))
print(result)