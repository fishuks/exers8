def text_output(function):
    def wrapped(parameter):
        result = function(parameter)
        print(result)
        return result
    return wrapped

# Функции для примера вывода 
@text_output
def simulation_1(numbers):
    return numbers

@text_output
def simulation_2(words):
    line = words.split()
    return line

numbers = input()
words = input()

simulation_1(numbers)
simulation_2(words)
